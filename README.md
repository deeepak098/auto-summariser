# 📝 AI Auto Summarizer

An AI-powered text summarization web application built with **Streamlit** and **Groq LLMs**. Paste any long article, blog, report, or notes, and the app generates a concise **3-sentence summary** along with **5 key takeaways** in seconds.

---

## 🚀 Features

* ✨ AI-generated summaries using Groq LLM
* 📄 Summarizes long text into exactly **3 sentences**
* 💡 Extracts **5 key takeaways**
* 📊 Displays:

  * Word count
  * Character count
  * Estimated reading time
* 📥 Download summary as a text file
* 🎨 Modern and responsive Streamlit interface
* 🔒 Secure API key management using `.env`

---

## 📸 Preview

> Add a screenshot of your application here.

Example:

```
📸 screenshot.png
```

---

## 🛠️ Tech Stack

* **Python**
* **Streamlit**
* **Groq API**
* **Llama 3.3 70B Versatile**
* **python-dotenv**

---

## 📂 Project Structure

```text
ai-auto-summarizer/
│
├── app.py               # Streamlit frontend
├── summarizer.py        # Groq API integration
├── prompts.py           # Prompt template
├── .env.example         # Environment variable template
├── requirements.txt
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/ai-auto-summarizer.git
```

### 2. Navigate into the project

```bash
cd ai-auto-summarizer
```

### 3. Create a virtual environment

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows**

```bash
python -m venv .venv
.venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Create a `.env` file

```env
GROQ_API_KEY=your_api_key_here
```

You can obtain a free API key from the Groq Console.

### 6. Run the application

```bash
streamlit run app.py
```

---

## 🧠 How It Works

1. The user pastes a long piece of text into the application.
2. The app calculates basic statistics such as word count, character count, and estimated reading time.
3. A structured prompt is dynamically generated using the input text.
4. The prompt is sent to the Groq API.
5. The LLM generates:

   * A concise **3-sentence summary**
   * **5 key takeaways**
6. The results are displayed in the Streamlit interface and can be downloaded as a text file.

---

## 📖 Key Concepts Learned

This project helped reinforce several AI Engineering concepts:

* Prompt Engineering
* Structured Prompting
* Large Language Model (LLM) API Integration
* Environment Variables with `.env`
* Modular Python Project Structure
* Streamlit UI Development
* Dynamic Prompt Generation
* Secure API Key Management
* Clean Separation of Frontend and Backend Logic

---

## 📦 Dependencies

```text
streamlit
groq
python-dotenv
```

---

## 🔮 Future Improvements

* Upload and summarize PDF documents
* Summarize web pages using URLs
* Summarize YouTube transcripts
* Support multiple summary lengths
* Tone selection (Professional, Academic, Simple)
* Copy summary to clipboard
* Export summaries as PDF
* Support multiple Groq models
* Return structured JSON responses for improved UI rendering

---

## 👨‍💻 Author

**Deepak Saladi**

If you found this project useful, feel free to ⭐ the repository and connect with me on GitHub.
