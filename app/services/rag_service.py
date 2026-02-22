from app.rag.loader import load_pdf
from app.rag.splitter import split_documents
from app.rag.retriever import get_retriever
from app.rag.chain import build_rag_chain
from app.models.embeddings import get_embeddings
from langchain_community.vectorstores import FAISS


class RAGService:
    """
    Production-style RAG service layer.
    Keeps business logic outside API routes.
    """

    def __init__(self):
        self.vectorstore = None

    def upload_policy(self, file_path: str):
        documents = load_pdf(file_path)
        chunks = split_documents(documents)

        embeddings = get_embeddings()

        self.vectorstore = FAISS.from_documents(
            documents=chunks,
            embedding=embeddings
        )

    def ask(self, question: str):
        if self.vectorstore is None:
            return {"error": "Upload a policy first"}

        retriever = get_retriever(self.vectorstore)
        docs = retriever.invoke(question)

        context = "\n\n".join([d.page_content for d in docs])

        sources = []
        for d in docs:
            if "page" in d.metadata:
                sources.append(f"Page {d.metadata['page'] + 1}")

        chain = build_rag_chain()

        response = chain.invoke({
            "context": context,
            "question": question
        })

        return {
            "answer": response.content,
            "sources": list(set(sources))
        }