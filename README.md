# ✦ Twinkle AI — Intelligent Search Assistant

Your own AI-powered search assistant built with Python, FastAPI, and Claude.

---

## 🚀 Quick Start in VS Code

### Step 1 — Open in VS Code
1. Unzip the project
2. Open VS Code → `File → Open Folder` → select `twinkle-ai/`

### Step 2 — Open Terminal in VS Code
Press `` Ctrl + ` `` (backtick) to open the terminal

### Step 3 — Install Dependencies
```bash
cd backend
pip install -r requirements.txt
```

### Step 4 — Add Your API Keys
Open `backend/.env` and replace the placeholder values:

```
ANTHROPIC_API_KEY=sk-ant-your-key-here
SERPER_API_KEY=your-serper-key-here
```

**Get your keys:**
- Anthropic API key → https://console.anthropic.com
- Serper API key (free) → https://serper.dev

### Step 5 — Run the Server
```bash
cd backend
python main.py
```

### Step 6 — Open in Browser
Visit: http://localhost:8000

---

## 📁 Project Structure

```
twinkle-ai/
├── backend/
│   ├── main.py          ← FastAPI server (start here)
│   ├── agent.py         ← AI brain (Claude integration)
│   ├── search.py        ← Web search (Serper API)
│   ├── config.py        ← Configuration & env vars
│   ├── requirements.txt ← Python dependencies
│   └── .env             ← Your API keys (never share!)
├── frontend/
│   └── index.html       ← Beautiful chat UI
├── Dockerfile           ← For cloud deployment
├── .gitignore
└── README.md
```

---

## 🌐 Deploy to Render (Free Hosting)

1. Push to GitHub:
```bash
git init
git remote add origin https://github.com/nehapythondeveloper2023-bot/twinkle-ai.git
git add .
git commit -m "Initial commit"
git branch -M main
git push -u origin main
```

2. Go to https://render.com → New Web Service
3. Connect your GitHub repo
4. Set **Build Command**: `pip install -r backend/requirements.txt`
5. Set **Start Command**: `cd backend && uvicorn main:app --host 0.0.0.0 --port $PORT`
6. Add environment variables: `ANTHROPIC_API_KEY` and `SERPER_API_KEY`
7. Click **Deploy** ✅

---

## 🔧 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + FastAPI |
| AI | Anthropic Claude |
| Search | Serper (Google Search API) |
| Frontend | HTML + CSS + JavaScript |
| Hosting | Render.com / Railway |

---

Built with ❤️ — Twinkle AI © 2026
