# 🤖 AI Q&A Assistant

AI-powered Q&A assistant that lets users provide any URL and ask questions based on its content. Built with LangChain & Groq for seamless AI-powered interactions.

---

## 🚀 Features

- 🔗 Provide any URL & ask questions about its content.
- 🧠 AI-powered responses using LangChain & Groq.
- 🎨 Modern & stylish UI with a glassmorphic design.
- ⚡ Fast & efficient API-based fetching.

---

## 🛠️ Tech Stack

- **Frontend:** HTML, CSS (Glassmorphism UI), JavaScript
- **Backend:** Python (FastAPI, LangChain, Groq API)
- **Database:** Not required (Real-time fetching)

---

## 🏗️ Setup Instructions

### 📥 Clone the Repository
```sh
git clone https://github.com/AbhishekL131/AI_Q-A_Assistant.git
cd AI_Q-A_Assistant
```

### 🔑 Set Up Environment Variables
Create a `.env` file and add your API keys:
```sh
touch .env
```
```ini
GROQ_API_KEY=your_api_key_here
```

### 📦 Install Dependencies
```sh
pip install -r requirements.txt
```

### ▶️ Run the Server
```sh
uvicorn main:app --reload
```

### 🌐 Open the Web App
Open `index.html` in your browser or use Live Server.

---

## ⚠️ Troubleshooting

### ❌ Remote Origin Already Exists
If you see:
```sh
error: remote origin already exists.
```
Fix it by running:
```sh
git remote remove origin
git remote add origin https://github.com/AbhishekL131/AI_Q-A_Assistant.git
```

### 🛑 .gitignore Not Working
If ignored files are still getting pushed:
```sh
git rm -r --cached .
git add .
git commit -m "Restored .gitignore"
git push origin main
```

---

## 🤝 Contributing
Pull requests & suggestions are welcome! Let's build something awesome. 💡✨

---

## 📜 License
This project is open-source under the MIT License.

