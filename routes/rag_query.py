from fastapi import APIRouter, Body
from rag.rag_pipeline import answer_with_rag

router = APIRouter()

@router.post("/rag-response")
def rag_response(query: str = Body(..., embed=True)):
    return {"response": answer_with_rag(query)}
