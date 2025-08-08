import streamlit as st
import requests

# --- PAGE CONFIG ---
st.set_page_config(page_title="SmartInterns", page_icon=":robot:", layout="wide")
st.title("🎯 Internship & Job Finder ")
st.write("Find jobs and internships based on your skills and interests.")

# --- API HEADERS ---
headers = {
    "X-RapidAPI-Key": st.secrets["rapi"]["key"],  # Save in .streamlit/secrets.toml
    "X-RapidAPI-Host": "jsearch.p.rapidapi.com"
}

# --- USER INPUT ---
skills = st.text_input("💻 Skills (e.g. Python, React)", key="skills_input")
domain = st.text_input("🎯 Domain or Role (e.g. Web Dev, Data Analyst)", key="domain_input")

# --- FUNCTION TO CALL API ---
@st.cache_data(ttl=3600)
def get_opportunities(query: str, num: int = 10):
    url = "https://jsearch.p.rapidapi.com/search"
    params = {
        "query": query,
        "page": "1",
        "num_pages": "1"
    }
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        return response.json().get("data", [])
    except Exception as e:
        st.error(f"❌ Error: {e}")
        return []

# --- DISPLAY FUNCTION ---
def show_opportunities(data, title):
    st.subheader(title)
    if not data:
        st.info("No results found.")
        return

    for item in data:
        job_title = item.get("job_title", "N/A")
        company = item.get("employer_name", "N/A")
        location = item.get("job_city", "N/A")
        url = item.get("job_apply_link", item.get("job_google_link", "#"))
        job_type = item.get("job_job_title", "N/A")
        employment_type = item.get("job_employment_type", "N/A")
        remote = item.get("job_is_remote", False)

        # ✅ Fix for date
        date_raw = item.get("job_posted_at_datetime_utc")
        date_posted = date_raw[:10] if date_raw else "N/A"

        # ✅ Fix for salary
        salary_info = item.get("job_salary") or {}
        salary = salary_info.get("salary", "Not specified")

        st.markdown(f"### 🔹 [{job_title}]({url})")
        st.markdown(f"- 🏢 **{company}**")
        st.markdown(f"- 📍 Location: *{location}*")
        st.markdown(f"- 🕒 Employment Type: *{employment_type}*")
        st.markdown(f"- 🌐 Remote: {'Yes' if remote else 'No'}")
        st.markdown(f"- 💰 Salary: {salary}")
        st.markdown(f"- 📅 Posted on: {date_posted}")
        st.markdown("---")



# --- BUTTON ---
if st.button("🔍 Search Opportunities"):
    if skills and domain:
        search_query = f"{skills} {domain} in India"
        with st.spinner("Fetching jobs and internships..."):
            data = get_opportunities(search_query)
            show_opportunities(data, "🚀 Results")
    else:
        st.warning("Please enter both skills and domain.")
