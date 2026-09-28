from fastapi import FastAPI

app = FastAPI(
    title="AI-Powered Professional Networking Assistant",
    description="AI assistant for personalized professional networking",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "AI-Powered Professional Networking Assistant API is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }
