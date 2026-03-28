# 🐞 AI Bug Fixer

An AI-powered debugging tool that detects errors in code, explains the issue, and suggests corrected solutions instantly.

---

## 🚀 Live Demo
👉 https://abhay-ai-bug-fixer.streamlit.app/

---

## 💡 Problem

Debugging code can be time-consuming and frustrating, especially for beginners and developers working under tight deadlines.

---

## 🧠 Solution

AI Bug Fixer uses Large Language Models (LLMs) to:
- Detect bugs in code
- Explain why the error occurs
- Suggest corrected and optimized code

---

## 🔥 Features

- 🐞 Bug Detection  
- 📖 Error Explanation  
- 🚀 Code Fix Suggestions  
- ⚡ Real-time AI responses  

---

## 🛠️ Tech Stack

- Python  
- Streamlit  
- Groq API (LLaMA 3)  

---

## 📂 Project Structure
ai-bug-fixer/ │ 
              ├── app/ │
                        └── app.py 
              ├── src/ │   
                       └── ai_engine.py 
              ├── requirements.txt 
              └── README.md
---

## ⚙️ How It Works

1. User pastes buggy code  
2. AI analyzes the code  
3. Identifies issues  
4. Explains the problem  
5. Suggests corrected version  

---

## 🧪 Example

### Input:
```python
x = 10
y = 0
print(x/y)
