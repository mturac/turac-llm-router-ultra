from fastapi import FastAPI, Request
from .router import SmartRouter

app = FastAPI(title="turac-llm-router-ultra")
router = SmartRouter()

@app.post("/v1/chat/completions")
async def chat_completions(request: Request):
    body = await request.json()
    return await router.route(body)

@app.get("/v1/models")
async def list_models():
    # OpenRouter gibi model listesi dönebilir
    return {"object": "list", "data": []}

@app.get("/health")
async def health():
    return {"status": "ok"}