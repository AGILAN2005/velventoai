import chromadb
from rag.embedder import get_embedding

client = chromadb.PersistentClient(path="chroma_db")
collection = client.get_or_create_collection(name="student_feedback")

def add_feedback_to_vector_db(student_id: str, feedback_text: str):
    embedding = get_embedding(feedback_text)
    collection.add(
        documents=[feedback_text],
        metadatas=[{"student_id": student_id}],
        ids=[f"{student_id}_{hash(feedback_text)}"]
    )

def get_similar_feedback(query: str, n_results: int = 3):
    query_embedding = get_embedding(query)
    results = collection.query(query_embeddings=[query_embedding], n_results=n_results)
    return results['documents'][0] if results['documents'] else []
