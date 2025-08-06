import streamlit as st
from serpapi import GoogleSearch
from typing import List, Tuple, Dict, Any

# --- Constants ---
SITES = [
    "site:internshala.com", "site:linkedin.com", "site:indeed.com",
    "site:naukri.com", "site:monsterindia.com", "site:letsintern.com",
    "site:glassdoor.co.in", "site:freshersworld.com", "site:hirect.in", "site:internships.com"
]
SITE_FILTER = " OR ".join(SITES)

# --- Page Config ---
st.set_page_config(page_title="Internship & Job Finder", layout="wide")

# --- Title ---
st.title("🎯 Internship & Job Finder")
st.write("Find opportunities in India based on your skills and interests.")

# --- Load SerpAPI Key from secrets.toml ---
try:
    API_KEY = st.secrets["api"]["serp_key"]
except (KeyError, FileNotFoundError):
    st.error("🚨 SerpAPI key not found. Please add it to your `.streamlit/secrets.toml` file.")
    st.stop()

# --- User Inputs ---
skills = st.text_input("💻 Enter your technical skills (comma-separated)", help="e.g., Python, SQL, React", key="skills_input")
interests = st.text_input("🎯 Enter your domain or career interest", help="e.g., Data Science, Web Dev", key="interests_input")

# --- Helper Functions ---

@st.cache_data(ttl="6h") # Cache results for 6 hours
def search_serpapi(query: str, api_key: str, count: int = 10) -> Dict[str, Any]:
    """
    Performs a Google search using the SerpApi.

    Args:
        query: The search query string.
        api_key: The SerpApi API key.
        count: The number of results to return.

    Returns:
        A dictionary containing the search results.
    
    Note: The api_key is included as an argument to ensure that if the key changes,
    the cache is invalidated. However, since it's sensitive, be mindful when
    using caching in different contexts.
    """
    params = {
        "engine": "google",
        "q": query,
        "api_key": api_key,
        "num": count,
        "location": "India"
    }
    search = GoogleSearch(params)
    return search.get_dict()

def display_results(results: List[Tuple[str, str, str]], header: str):
    """
    Displays a list of search results in a Streamlit expander.

    Args:
        results: A list of tuples, where each tuple contains (title, link, snippet).
        header: The text to display for the expander.
    """
    with st.expander(header, expanded=True):
        if results:
            for i, (title, link, snippet) in enumerate(results, 1):
                st.markdown(f"**{i}. [{title}]({link})**")
                st.markdown(f"📝 {snippet}")
                st.markdown("---")
        else:
            st.info(f"No {header.lower()} found for your query.")

def process_and_display_internships(results_dict: Dict[str, Any]):
    """
    Processes internship results, categorizes them as paid or free, and displays them.
    """
    st.subheader("🎓 Internships")
    if "organic_results" not in results_dict:
        st.warning("No internship listings found or an error occurred.")
        return

    free_internships = []
    paid_internships = []

    for result in results_dict.get("organic_results", []):
        title = result.get("title", "No Title")
        link = result.get("link", "#")
        snippet = result.get("snippet", "").lower()

        # Simple categorization based on keywords
        if "stipend" in snippet or "paid" in snippet or "₹" in snippet:
            paid_internships.append((title, link, snippet))
        else:
            free_internships.append((title, link, snippet))

    display_results(paid_internships, "💰 Paid Internships")
    display_results(free_internships, "🎓 Unpaid/Unspecified Internships")

def process_and_display_jobs(results_dict: Dict[str, Any]):
    """
    Processes job results and displays them.
    """
    st.subheader("💼 Job Opportunities")
    if "organic_results" not in results_dict:
        st.warning("No job listings found or an error occurred.")
        return

    job_list = []
    for result in results_dict.get("organic_results", []):
        title = result.get("title", "No Title")
        link = result.get("link", "#")
        snippet = result.get("snippet", "No description available.")
        job_list.append((title, link, snippet))

    display_results(job_list, "Available Jobs")

def display_skill_suggestions(interests: str):
    """
    Displays skill suggestions based on user's interests.
    """
    st.subheader("📈 Skill Suggestions")
    interest_lower = interests.lower()
    suggestions_made = False

    if "data" in interest_lower:
        st.markdown("- **For Data Roles:** Learn Python (Pandas, NumPy), SQL, Excel, and visualization tools like Tableau or Power BI.")
        suggestions_made = True
    if "web" in interest_lower:
        st.markdown("- **For Web Development:** Master HTML, CSS, JavaScript. Explore frameworks like React.js, Angular, or Vue.js for frontend, and Node.js, Django, or Flask for backend.")
        suggestions_made = True
    if "android" in interest_lower:
        st.markdown("- **For Android Development:** Try Kotlin or Java for native development, or Flutter for cross-platform apps. Get familiar with Android Studio.")
        suggestions_made = True
    if "ai" in interest_lower or "ml" in interest_lower:
        st.markdown("- **For AI/ML:** Work on projects using scikit-learn, TensorFlow, or PyTorch. Explore libraries like Hugging Face for NLP and OpenCV for computer vision.")
        suggestions_made = True

    if not suggestions_made:
        st.info("Could not generate specific skill suggestions. Try broadening your interest, e.g., 'web development', 'data science'.")

# --- Main Application Logic ---
if st.button("🔍 Find Opportunities"):
    if skills and interests:
        with st.spinner("Searching for opportunities... 🕵️‍♂️"):
            # Build queries
            internship_query = f"{interests} internship in India for {skills} {SITE_FILTER}"
            job_query = f"{interests} jobs in India for {skills} {SITE_FILTER}"

            # Perform searches
            internship_results = search_serpapi(internship_query, API_KEY)
            job_results = search_serpapi(job_query, API_KEY)

        # Display results outside the spinner
        if internship_results or job_results:
            process_and_display_internships(internship_results)
            process_and_display_jobs(job_results)
            display_skill_suggestions(interests)
        else:
            st.error("An error occurred while searching. Please try again.")
    else:
        st.warning("⚠️ Please enter both skills and interests to search.")
else:
    st.info("👆 Please enter your skills and interests to begin.")
