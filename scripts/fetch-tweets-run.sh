#!/bin/bash
KEY="$XAI_API_KEY"
if [ -z "$KEY" ]; then
  echo "ERROR: XAI_API_KEY not set"
  exit 1
fi

FROM_DATE="2026-04-10"
TO_DATE="2026-04-17"

QUERY="Search X for: tweets from @shawnmakesmagic, @a1lon9, @AzFlin and also find who are the top 5 people each of them follow and get recent tweets from those people too. Date range: ${FROM_DATE} to ${TO_DATE}. For each person, return their most interesting/insightful/highly-engaged recent tweets. Include: @handle, full text, date posted, engagement (likes/retweets if available), and direct link (https://x.com/handle/status/ID). Organize by person. Be thorough."

BODY=$(cat <<ENDJSON
{
  "model": "grok-4-1-fast",
  "input": [{"role": "user", "content": "$QUERY"}],
  "tools": [{"type": "x_search", "from_date": "$FROM_DATE", "to_date": "$TO_DATE"}]
}
ENDJSON
)

curl -s -X POST "https://api.x.ai/v1/responses" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $KEY" \
  -d "$BODY"
