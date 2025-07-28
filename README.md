# 📘 LeetCode Scraper

A Python-based LeetCode scraper to fetch:
1. ✅ Your LeetCode username
2. 📊 Total number of questions solved
3. 📋 All accepted submissions (question name, time, status, etc.)

---

## 🛠 Requirements

Install dependencies from the `requirements.txt`:

```bash
pip install -r requirements.txt
```


requirements.txt should contain:
```bash
requests
python-dotenv
```

🔐 Setup .env
Create a .env file in the root folder:

env
Copy
Edit
LEETCODE_SESSION=your_session_id_here
CSRFTOKEN=your_csrf_token_here
🔍 How to get LEETCODE_SESSION and CSRFTOKEN:
Open leetcode.com and log in.

Right-click → Inspect → go to Application tab.

On the left, select Cookies > https://leetcode.com

Copy values for:

LEETCODE_SESSION

csrftoken

Paste them into your .env file.

📸 Screenshot Example:

(Insert image here showing browser devtools and cookie section)

📁 Project Files
File	Description
get_username.py	Prints your LeetCode username using session cookie
get_total_solved.py	Fetches total number of accepted problems
scrape_all_questions.py	Scrapes all accepted submissions with timestamps (deduplicated)

🚀 Usage
Run each script individually:

bash
Copy
Edit
python get_username.py
python get_total_solved.py
python scrape_all_questions.py
📦 Output
get_username.py
bash
Copy
Edit
✅ Logged in as: alok_jha
get_total_solved.py
bash
Copy
Edit
📊 Total Solved Questions: 224
scrape_all_questions.py
bash
Copy
Edit
📥 Fetching all accepted submissions...
✅ Total unique accepted questions: 224
💾 Saved to solved_questions.json
📸 Screenshots:

(Leave space here to add actual screenshots of terminal output + generated solved_questions.json preview)

📄 License
This project is licensed under the MIT License.

vbnet
Copy
Edit

Let me know if you'd like me to generate the actual `README.md` file or push structure suggestions for your GitHub repo