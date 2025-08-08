# 🤖 AI-Powered Internship & Job Finder

[![Streamlit App](https://img.shields.io/badge/🚀%20Live%20App-SmartIntern-green?style=for-the-badge)](https://smartintern.streamlit.app/)
![Made with Streamlit](https://img.shields.io/badge/Built%20with-Streamlit-orange?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge)

---

## 🔍 What is SmartIntern?

**SmartIntern** is an AI-powered Streamlit application that helps students and freshers discover relevant **internship and job opportunities** in India based on their **skills and interests**.

It leverages the **SerpAPI Google Search API** to pull real-time results from platforms like:
- Internshala
- Naukri
- LinkedIn
- Indeed
- glassdoor
- Freshersworld and more

---

## ✨ Features

✅ Search for both **Internships** and **Full-Time Jobs**  
✅ Filters job listings from **top Indian job sites**  
✅ AI-based skill suggestion from interest keywords  
✅ Smart categorization: **Paid vs Unpaid internships**  
✅ Fast, intuitive and minimal UI using **Streamlit**  
✅ Powered by real-time **Google search results**

---

## 🚀 Live Demo

🔗 Click here to try it out:  
👉 **[https://smartintern.streamlit.app/](https://smartintern.streamlit.app/)**
🔗 Backup Link:  
👉 **[https://smartinterns.streamlit.app/](https://smartinterns.streamlit.app/)**


---

## ⚙️ Setup Instructions

### ✅ Prerequisites

- Python 3.8 or above
- A free API key from [SerpAPI](https://serpapi.com/)

---

### 🛠️ Setup Steps

1.  **Clone the Repository**

    ```bash
    git clone https://github.com/Yashas8gatty/IBM-AI.git
    cd IBM-AI
    ```

2.  **Create a Virtual Environment**

    ```bash
    # For Windows
    python -m venv venv
    venv\Scripts\activate

    # For macOS/Linux
    python3 -m venv venv
    source venv/bin/activate
    ```

3.  **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure API Key**

    Use Streamlit secrets to store your SerpAPI key securely:

    ```toml
    # 📁 .streamlit/secrets.toml
    [api]
    serp_key = "YOUR_SERPAPI_KEY"
    ```
    ⚠️ Do not commit this file! It's excluded in `.gitignore`.

5.  **Run the App**

    ```bash
    streamlit run app.py
    ```
    The app will open in your browser. Enter your skills and interests to get personalized job listings.

---

### 🖼️ Optional: Screenshots
You can upload screenshots of the interface and uncomment below:

<!-- ### 🔎 Home Page !Home ### 📋 Filtered Results !Results -->

---
### TEAM NAME : DATA REGIME
### 👥 Team Members
- Yashas H Gatty
- Uttham
- Sanjana Mahale
- P Harshitha
- Vrinda B Kumtakar
- Reeshal Dsouza
- Puneeth
- Srujan Ds

---

### 🧠 Tech Stack
- Python 3.8+
- Streamlit
- SerpAPI
- HTML Parsing & Filtering
- GitHub Collaboration

---



---

### 🙌 Support or Feedback?
Have suggestions or ideas?
Feel free to open an issue or create a pull request.
