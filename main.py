from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from groq_client import get_feedback

app = FastAPI()

# CORS (required for local frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/analyze")
async def analyze(
    video: UploadFile = File(...),
    action: str = Form(...)
):
    # IMPORTANT: read video as BYTES, but DO NOT return it
    video_bytes = await video.read()

    # ---- MOCK METRICS FOR NOW ----
    metrics = {
        "knee_angle": 140,
        "trunk_lean": 10,
        "head_stable": True
    }

    rules = {
        "knee_ok": 130 <= metrics["knee_angle"] <= 160,
        "lean_ok": metrics["trunk_lean"] < 15,
        "head_ok": metrics["head_stable"]
    }

    feedback = get_feedback(action, metrics, rules)

    # ✅ RETURN ONLY JSON-SAFE DATA
    return feedback
