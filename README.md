# TalentScout – AI Hiring Assistant 🤖

TalentScout is an AI-powered hiring assistant that conducts interactive candidate interviews.  
It collects candidate details, asks technical questions based on their tech stack, and saves results for later review.  
The app is built with **Streamlit** and powered by **Google Gemini AI**.

---

## 📑 Table of Contents
- [Introduction](#-introduction)
- [Features](#-features)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Project Structure](#-project-structure)
- [Dependencies](#-dependencies)
- [Example Interview Flow](#-example-interview-flow)
- [Troubleshooting](#-troubleshooting)

---

## 🚀 Introduction
TalentScout acts as an **AI hiring chatbot**. It guides candidates through an interview process by:

- Collecting basic details: **name, email, phone, experience, position, location, tech stack**  
- Conducting a **technical Q&A session** with context-aware follow-up questions  
- Saving candidate responses to a JSON file for later review  

---

## ✨ Features
✅ Collects structured candidate information  
✅ Dynamic, context-driven technical interview powered by **Gemini AI**  
✅ Adapts **follow-up questions** based on candidate answers  
✅ Interactive **chat interface** using Streamlit  
✅ Saves candidate profiles in `candidate_data.json`  
✅ Restart interviews seamlessly within the app  

---

## ⚙️ Installation
Clone the repository and install dependencies:

```
git clone https://github.com/your-username/talentscout.git
cd talentscout
pip install -r requirements.txt
```

---

## 🔑 Configuration
Create a `.env` file in the project root and add your **Google Gemini API key**:

```
GEMINI_API_KEY=your_api_key_here
```

⚠️ If the key is missing, the app will not start.

---

## ▶️ Usage
Run the Streamlit app:

```
streamlit run app.py
```

- Open the provided local URL in your browser.  
- The chatbot begins by greeting the candidate.  
- Candidates provide their details step by step.  
- Once the **tech stack** is shared, AI-generated technical questions begin.  
- Interview ends with a thank-you message and the candidate data gets saved.  

---

## 📂 Project Structure
```
.
├── app.py # Streamlit front-end
├── interview_bot.py # InterviewBot class handling logic & AI calls
├── prompts.py # System and technical question prompts
├── requirements.txt # Project dependencies
├── candidate_data.json # Saved candidate interviews (created at runtime)
└── .env # API key configuration (user-provided)
```

---

## 📦 Dependencies
From `requirements.txt`:

- **streamlit** – UI framework for interactive app  
- **python-dotenv** – Load API keys from `.env`  
- **google-generativeai** – Gemini API client for AI-driven interview questions  

---

## 💬 Example Interview Flow

Bot: "Let's get started. Please tell me your full name."
Candidate: "Jane Doe"

Bot: "Please provide your email address."
… (collects phone, experience, position, location, tech stack)

Bot: "Let's begin the technical round. Can you explain how memory management works in Python?"
Candidate: "It uses reference counting with garbage collection."

Bot: "Good point. Can you give an example where garbage collection is triggered?"
… (up to 5 questions total).

Bot: "That concludes the technical round. Thank you for your answers!"


---

## 🛠️ Troubleshooting
- **Error: `GEMINI_API_KEY` missing** → Add it to `.env`  
- **Interview not progressing** → Ensure valid input; empty responses prompt the bot to request clarification  
- **No candidate data saved** → Check file permissions for `candidate_data.json`  
