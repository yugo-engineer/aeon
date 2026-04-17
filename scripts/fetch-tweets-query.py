import os
import json
import urllib.request
import sys

api_key = os.environ.get("XAI_API_KEY", "")
if not api_key:
    print("ERROR: XAI_API_KEY not set")
    sys.exit(1)

from_date = "2026-04-10"
to_date = "2026-04-17"

query = (
    "Search X for: tweets from @shawnmakesmagic, @a1lon9, @AzFlin "
    "and also find who are the top 5 people each of them follow and "
    "get recent tweets from those people too. Date range: "
    + from_date + " to " + to_date + ". For each person, return their most "
    "interesting/insightful/highly-engaged recent tweets. Include: "
    "@handle, full text, date posted, engagement (likes/retweets if "
    "available), and direct link (https://x.com/handle/status/ID). "
    "Organize by person. Be thorough."
)

payload = {
    "model": "grok-4-1-fast",
    "input": [{"role": "user", "content": query}],
    "tools": [{"type": "x_search", "from_date": from_date, "to_date": to_date}]
}

req = urllib.request.Request(
    "https://api.x.ai/v1/responses",
    data=json.dumps(payload).encode(),
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + api_key
    },
    method="POST"
)

try:
    with urllib.request.urlopen(req, timeout=120) as resp:
        data = resp.read().decode()
        print(data)
except Exception as e:
    print("ERROR: " + str(e))
    sys.exit(1)
