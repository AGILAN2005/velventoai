from rag.retriever import retrieve_similar_docs
from utils.gemini_api import call_gemini  # Assumes you already have Gemini wrapper

def answer_with_rag(query: str) -> str:
    context = retrieve_similar_docs(query)
    prompt = f"""You are a learning assistant. Use the following context from the student's learning history to provide an adaptive response.

Context:
{context}

Now answer this question or generate feedback:
{query}"""
    return call_gemini(prompt)
