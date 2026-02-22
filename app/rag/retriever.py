def get_retriever(vectorstore):
    """
    Converts a vectorstore into a retriever.
    This allows semantic searching using invoke().
    """

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": 3}  # return top 3 chunks
    )

    return retriever