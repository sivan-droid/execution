from fastapi import FastAPI
from pydantic import BaseModel

from graph.graph_builder import build_graph

app = FastAPI()

graph = build_graph()


class SummaryRequest(BaseModel):
    text: str


@app.get("/")
def health():
    return {
        "status": "running",
        "agent": "LangGraph Groq Summarizer"
    }


@app.post("/summarize")
def summarize(req: SummaryRequest):

    result = graph.invoke({
        "input_text": req.text
    })

    return {
        "success": True,
        "summary": result["summary"]
    }