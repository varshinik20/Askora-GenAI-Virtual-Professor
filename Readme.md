# Askora: GenAI Virtual Professor 🎓

Askora is an interactive, multilingual AI-powered educational web application designed to act as a 24/7 personal tutor. It delivers comprehensive academic explanations, generates real-time multilingual neural speech, and synchronizes responses with an animated virtual professor avatar.

---

## ✨ Features

- 📚 **Multi-Subject Tutoring**: Covers subjects including Mathematics, Physics, Chemistry, Biology, Computer Science, AI, Machine Learning, Data Structures, Operating Systems, and General Topics.
- 🌐 **Multilingual Support**: Supports **English**, **Tamil (தமிழ்)**, and **Hindi (हिन्दी)** with native system prompts.
- ⚡ **Ultra-Fast AI Explanations**: Powered by Groq's high-speed LLaMA 3.1 model (`llama-3.1-8b-instant`).
- 🎙️ **Neural Text-to-Speech (TTS)**: Realistic speech synthesis using Microsoft Edge TTS with high-quality multilingual voices.
- 🎥 **Animated Avatar Synchronization**: Real-time video playback synchronized with speech and responsive status indicators (Thinking / Speaking / Idle).

---

## 🛠️ Tech Stack

- **Backend**: Python, Flask, Flask-CORS, AsyncIO
- **LLM Engine**: Groq API (`llama-3.1-8b-instant`)
- **Speech Engine**: Microsoft `edge-tts`
- **Frontend**: HTML5, CSS3, Vanilla JavaScript (Poppins font, dynamic sidebar, glassmorphic UI)

---

## 📂 Project Structure

```
virtual_professor/
├── backend/
│   ├── app.py                 # Flask server & TTS generation endpoint
│   ├── genai_engine.py       # Groq API integration
│   ├── language_module.py    # Multilingual configurations & prompts
│   ├── requirements.txt      # Backend Python dependencies
│   ├── static/
│   │   ├── professor.mp4     # Animated professor avatar video
│   │   ├── script.js         # Frontend logic & media synchronization
│   │   └── style.css         # UI stylesheet
│   └── templates/
│       └── index.html        # Main web interface
├── requirements.txt          # Root Python dependencies
└── Readme.md                 # Project documentation
```

---

## 🚀 Getting Started

### 1. Prerequisites
- Python 3.9+
- A Groq API key (from [console.groq.com](https://console.groq.com))

### 2. Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/varshinik20/Askora-GenAI-Virtual-Professor.git
   cd Askora-GenAI-Virtual-Professor/backend
   ```

2. **Create and activate a virtual environment**:
   ```bash
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the `backend/` directory:
   ```env
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the Application**:
   ```bash
   python app.py
   ```

6. **Access the App**:
   Open `http://localhost:5000` in your web browser.
