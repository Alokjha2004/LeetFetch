import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")
CSRFTOKEN = os.getenv("CSRFTOKEN")

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": "https://leetcode.com",
    "x-csrftoken": CSRFTOKEN,
    "Content-Type": "application/json",
    "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRFTOKEN};"
}

url = "https://leetcode.com/graphql"

payload = {
    "query": """
        query {
            userStatus {
                username
                isSignedIn
            }
        }
    """
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    data = response.json()
    user = data.get("data", {}).get("userStatus", {})
    if user.get("isSignedIn"):
        print(f"✅ Logged in as: {user['username']}")
    else:
        print("❌ Cookie valid but not logged in.")
else:
    print(f"❌ Error: {response.status_code}")
    print(response.text[:300])
