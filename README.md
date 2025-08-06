# 🎯 Internship & Job Finder

A simple Streamlit application to find internship and job opportunities in India based on your skills and interests. This tool uses the SerpApi Google Search API to query multiple job portals simultaneously.

## ✨ Features

-   Search for both internships and jobs.
-   Filter results from popular Indian job sites like Internshala, LinkedIn, Naukri, etc.
-   Automatically categorizes internships into "Paid" and "Unpaid/Unspecified" based on listing details.
-   Provides skill suggestions based on your career interests.
-   Simple and intuitive user interface built with Streamlit.

## 🚀 Setup and Installation

Follow these steps to get the application running on your local machine.

### Prerequisites

-   Python 3.8+
-   A SerpApi API Key. You can get one for free from [serpapi.com](https://serpapi.com/).

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd <your-repo-name>
```

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```bash
# For Windows
python -m venv venv
venv\Scripts\activate

# For macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

Install the required Python packages using the `requirements.txt` file.

```bash
pip install -r requirements.txt
```

### 4. Configure API Key

This application uses Streamlit's secrets management.

1.  Create a directory named `.streamlit` in the root of the project.
2.  Inside `.streamlit`, create a file named `secrets.toml`.
3.  Add your SerpApi key to this file in the following format:

    ```toml
    # .streamlit/secrets.toml
    [api]
    serp_key = "YOUR_SERPAPI_KEY_HERE"
    ```

**Important:** The `secrets.toml` file is included in `.gitignore` and should **never** be committed to your repository to keep your API key private.

## 🏃‍♀️ Running the Application

Once the setup is complete, you can run the Streamlit app with the following command:

```bash
streamlit run app.py
```

Your web browser should open a new tab with the application running. Enter your skills and interests to start finding opportunities!