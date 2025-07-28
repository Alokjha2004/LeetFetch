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
---

## 🔐 Setup .env
Create a .env file in the root folder:

```bash
LEETCODE_SESSION = your_session_id_here
CSRFTOKEN = your_csrf_token_here
```

---


## 🔍 How to get `LEETCODE_SESSION` and `CSRFTOKEN`:

1. Open [leetcode.com](https://leetcode.com) and log in.  
2. Right-click → Inspect → go to the **Application** tab.  
3. On the left sidebar, select **Cookies > https://leetcode.com**  
4. Copy values for:  
   - `LEETCODE_SESSION`  
   - `csrftoken`  
5. Paste them into your `.env` file.

### 📸 **Screenshot Example**:  

<img width="800" height="449" alt="Screenshot 2025-07-28 200153" src="https://github.com/user-attachments/assets/2ec1531b-a074-4309-b4d4-2b6a71c03d55" />


--- 

## 📁 Project
 Files

| File                    | Description                                             |
|-------------------------|---------------------------------------------------------|
| `get_username.py`       | Prints your LeetCode username using session cookie      |
| `get_total_solved.py`   | Fetches total number of accepted problems               |
| `scrape_all_questions.py` | Scrapes all accepted submissions with timestamps (deduplicated) |

---

## 🚀 Usage

Run each script individually:

```bash
python get_username.py
python get_total_solved.py
python scrape_all_questions.py
```
--- 

## 📦 Output

### `get_username.py`

```bash
✅ Logged in as: alok_jha
```

### `get_total_solved.py`

```bash
📊 Total Solved Questions: 224
```

### `scrape_all_questions.py`

```bash
📥 Fetching all accepted submissions...
✅ Total unique accepted questions: 224
💾 Saved to solved_questions.json
```
📸 Screenshots:

(Leave space here to add actual screenshots of terminal output + generated solved_questions.json preview)

---

## 📄 License
This project is licensed under the MIT License.
