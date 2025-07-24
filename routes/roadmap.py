from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel
from duckduckgo_search import DDGS
from utils.gemini import generate_roadmap_stages

router = APIRouter()

class RoadmapRequest(BaseModel):
    user_id: str
    topic: str

@router.post("/generate-roadmap/")
async def generate_roadmap(data: RoadmapRequest):
    # 1. Search DuckDuckGo
    with DDGS() as ddgs:
        results = ddgs.text(f"{data.topic} learning roadmap", max_results=50)
        links = [r["href"] for r in results if "href" in r]

    if not links:
        raise HTTPException(status_code=404, detail="No links found")

    # 2. Summarize into stages using Gemini
    roadmap = generate_roadmap_stages(data.topic, links)

    return {
        "user_id": data.user_id,
        "topic": data.topic,
        "roadmap": roadmap
    }
