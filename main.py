from fastapi import FastAPI
from rules import evaluate
from groq_client import get_feedback

app = FastAPI()

@app.post("/analyze")
def analyze(data: dict):
    rules = evaluate(data["metrics"])
    return get_feedback(data["action"], data["metrics"], rules)
