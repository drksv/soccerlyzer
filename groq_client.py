import os
from groq import Groq
from dotenv import load_dotenv

# Load .env variables
load_dotenv()

# Get API key from environment
GROQ_API_KEY = os.getenv("SOCCERANALYZER_GROQ_API_KEY")

if not GROQ_API_KEY:
    raise ValueError("GROQ API key not found in .env file")

client = Groq(api_key=GROQ_API_KEY)


def get_feedback(action, metrics, rules):
    prompt = f"""
You are a football coach.
Action: {action}
Metrics: {metrics}
Flags: {rules}

Return ONLY 4 short lines:
1 good thing
2 fixes
1 simple drill
No jargon.
"""

    res = client.chat.completions.create(
        model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=120
    )

    lines = [l.strip() for l in res.choices[0].message.content.split("\n") if l.strip()]

    return {
        "good": lines[0] if len(lines) > 0 else "",
        "fix1": lines[1] if len(lines) > 1 else "",
        "fix2": lines[2] if len(lines) > 2 else "",
        "drill": lines[3] if len(lines) > 3 else ""
    }
