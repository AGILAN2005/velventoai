from rag.chroma_db import get_similar_feedback

def retrieve_similar_docs(query: str) -> str:
    docs = get_similar_feedback(query)
    return "\n\n".join(docs)
