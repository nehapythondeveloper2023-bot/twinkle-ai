from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
from agent import twinkle_respond
import os

app = FastAPI(
    title="Twinkle AI",
    description="Your intelligent search assistant",
    version="1.0.0"
)

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class QueryRequest(BaseModel):
    query: str


class QueryResponse(BaseModel):
    answer: str
    sources: list


@app.post("/search", response_model=QueryResponse)
async def search(req: QueryRequest):
    """Main search endpoint — searches web and returns AI answer"""
    if not req.query.strip():
        raise HTTPException(status_code=400, detail="Query cannot be empty")

    try:
        result = await twinkle_respond(req.query)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/health")
def health():
    """Health check endpoint"""
    return {"status": "Twinkle AI is running ✨", "version": "1.0.0"}


# Serve the frontend (index.html)
frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend")
if os.path.exists(frontend_path):
    app.mount("/static", StaticFiles(directory=frontend_path), name="static")

    @app.get("/")
    def serve_frontend():
        return FileResponse(os.path.join(frontend_path, "index.html"))


if __name__ == "__main__":
    import uvicorn
    from config import APP_HOST, APP_PORT
    uvicorn.run("main:app", host=APP_HOST, port=APP_PORT, reload=True)
