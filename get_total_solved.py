import os
import requests

from dotenv import load_dotenv
load_dotenv()


LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")
CSRFTOKEN = os.getenv("CSRFTOKEN")
USERNAME = "your_username"  # Replace with your actual LeetCode username

headers = {
    "User-Agent": "Mozilla/5.0",
    "Referer": f"https://leetcode.com/{USERNAME}/",
    "x-csrftoken": CSRFTOKEN,
    "Content-Type": "application/json",
    "Cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRFTOKEN};"
}

url = "https://leetcode.com/graphql"

payload = {
    "query": """
    query getUserProfile($username: String!) {
      allQuestionsCount {
        difficulty
        count
      }
      matchedUser(username: $username) {
        submitStatsGlobal {
          acSubmissionNum {
            difficulty
            count
          }
        }
      }
    }
    """,
    "variables": {"username": USERNAME}
}

response = requests.post(url, headers=headers, json=payload)

if response.status_code == 200:
    data = response.json()
    solved = data["data"]["matchedUser"]["submitStatsGlobal"]["acSubmissionNum"]
    total = sum(item["count"] for item in solved)
    
    print(f"\n✅ Total Questions Solved by {USERNAME}: {total}")
    for item in solved:
        print(f"  {item['difficulty']}: {item['count']} solved")
else:
    print(f"❌ Error: {response.status_code}")
    print(response.text[:300])
