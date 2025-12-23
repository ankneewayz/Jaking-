import json, requests

GROQ_API_KEY = "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"

def handler(request):
    try:
        body = json.loads(request.data)
        r = requests.post(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {GROQ_API_KEY}",
                "Content-Type": "application/json"
            },
            json=body
        )
        return (r.content, 200, {"Content-Type":"application/json"})
    except Exception as e:
        return (json.dumps({"error":str(e)}), 500, {"Content-Type":"application/json"})