import os
import time
import json
import requests
from dotenv import load_dotenv
load_dotenv()


LEETCODE_SESSION = os.getenv("LEETCODE_SESSION")
CSRFTOKEN = os.getenv("CSRFTOKEN")


HEADERS = {
    "cookie": f"LEETCODE_SESSION={LEETCODE_SESSION}; csrftoken={CSRFTOKEN};",
    "x-csrftoken": CSRFTOKEN,
    "referer": "https://leetcode.com",
    "Content-Type": "application/json",
    "User-Agent": "Mozilla/5.0"
}

GRAPHQL_URL = "https://leetcode.com/graphql"
CHECKPOINT_FILE = "checkpoint.json"
RESULT_FILE = "solved_questions.json"

def save_checkpoint(cursor, data):
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump({"cursor": cursor, "data": data}, f)

def load_checkpoint():
    if os.path.exists(CHECKPOINT_FILE):
        with open(CHECKPOINT_FILE, "r") as f:
            cp = json.load(f)
            return cp.get("cursor"), cp.get("data", {})
    return None, {}

def fetch_graphql(cursor=None):
    query = """
    query Submissions($offset: Int!, $limit: Int!) {
        submissionList(offset: $offset, limit: $limit) {
            hasNext
            submissions {
                id
                title
                titleSlug
                statusDisplay
                timestamp
            }
        }
    }
    """

    offset = int(cursor) if cursor else 0
    payload = {
        "operationName": "Submissions",
        "variables": {"offset": offset, "limit": 20},
        "query": query
    }

    response = requests.post(GRAPHQL_URL, headers=HEADERS, json=payload)
    if response.status_code == 200:
        return response.json(), offset
    else:
        raise Exception(response.status_code)

def main():
    print("📥 Fetching all accepted submissions with cursor and checkpoint...")
    cursor, accepted_data = load_checkpoint()
    offset = int(cursor) if cursor else 0

    retries = 0
    max_retries = 5

    while True:
        try:
            result, offset = fetch_graphql(offset)
            retries = 0  # reset on success
        except Exception as e:
            code = str(e)
            print(f"[⏳] Error {code} at offset {offset}. Retrying in {2**retries}s...")
            time.sleep(2 ** retries)
            retries += 1
            if retries > max_retries:
                print(f"[⚠️] Skipping offset {offset} due to repeated failure.")
                break
            continue

        submissions = result["data"]["submissionList"]["submissions"]
        if not submissions:
            break

        for sub in submissions:
            if sub["statusDisplay"] == "Accepted":
                title_slug = sub["titleSlug"]
                timestamp = sub["timestamp"]
                if (title_slug not in accepted_data or 
                    int(timestamp) > int(accepted_data[title_slug]["timestamp"])):
                    accepted_data[title_slug] = {
                        "title": sub["title"],
                        "title_slug": title_slug,
                        "timestamp": timestamp
                    }

        offset += 20
        save_checkpoint(offset, accepted_data)

        if not result["data"]["submissionList"]["hasNext"]:
            break

    final_data = []
    for q in accepted_data.values():
        final_data.append({
            "title": q["title"],
            "title_slug": q["title_slug"],
            "solved_at": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(q["timestamp"])))
        })

    final_data.sort(key=lambda x: x["solved_at"], reverse=True)

    with open(RESULT_FILE, "w", encoding="utf-8") as f:
        json.dump(final_data, f, indent=2)

    print(f"✅ Total unique accepted questions: {len(final_data)}")
    print(f"💾 Saved to {RESULT_FILE}")


if __name__ == "__main__":
    main()
