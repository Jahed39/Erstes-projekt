import json
import urllib.request

def analyse_stimmung(text: str) -> dict:
    payload = json.dumps({
        "model": "llama3.2",
        "prompt": f"""Respond with ONLY a JSON object, no other text:
{{"stimmung": "positiv", "score": 7, "emotion": "Freude", "kurzfazit": "Ein guter Tag."}}

Now analyze this diary entry and respond with ONLY JSON in that exact format:
{text}""",
        "stream": False,
        "format": "json"
    }).encode()

    req = urllib.request.Request(
        "http://localhost:11434/api/generate",
        data=payload,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req) as res:
        result = json.loads(res.read())

    return json.loads(result["response"])