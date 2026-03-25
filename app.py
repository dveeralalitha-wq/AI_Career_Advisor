import streamlit as st
from resume_parser import extract_resume_text
from utils import calculate_resume_score
from recommender import (
    recommend_roles,
    recommend_skills,
    recommend_industries,
    career_path,
    recommend_courses
)

# Page Config
st.set_page_config(page_title="AI Career Guidance", layout="wide")

st.title("🚀 AI Career Guidance System")

# ================= INPUT SECTION ================= #

st.header("📥 Enter Your Details")

education = st.selectbox(
    "Education Level",
    ["High School", "Bachelor’s", "Master’s"]
)

skills = st.text_input(
    "Enter your skills (comma separated)",
    placeholder="Python, SQL, Excel"
)

skills_list = [s.strip().lower() for s in skills.split(",") if s]

interest = st.selectbox(
    "Career Interest",
    ["Data Science", "AI / ML", "Banking", "Software Development"]
)

experience = st.text_area(
    "Work Experience / Projects",
    placeholder="Describe your projects or internships..."
)

location = st.selectbox(
    "Location Preference",
    ["City", "Remote", "Any"]
)

resume_file = st.file_uploader(
    "Upload Resume (PDF/DOCX)",
    type=["pdf", "docx"]
)

# ================= ANALYZE BUTTON ================= #

if st.button("🔍 Analyze"):

    st.header("📊 Analysis Results")

    # Extract resume text
    resume_text = ""
    if resume_file:
        try:
            resume_text = extract_resume_text(resume_file)
        except Exception as e:
            st.error("Error reading resume file. Please upload a valid file.")
    else:
        st.warning("⚠️ Resume not uploaded. Score will be limited.")

    # Calculate score
    score, feedback = calculate_resume_score(resume_text, skills_list)

    # ================= SCORE ================= #
    st.subheader("🎯 Resume Score")
    st.metric(label="Your Score", value=f"{score}/100")

    # ================= FEEDBACK ================= #
    st.subheader("📝 Resume Feedback")

    if feedback:
        for f in feedback:
            st.write(f"✔ {f}")
    else:
        st.success("Great! Your resume looks strong.")

    # ================= RECOMMENDATIONS ================= #

    roles = recommend_roles(skills_list, interest)
    rec_skills = recommend_skills(skills_list, interest)
    industries = recommend_industries(interest)
    path = career_path(interest)
    courses = recommend_courses(interest)

    # JOB ROLES
    st.subheader("💼 Suggested Job Roles")
    for r in roles:
        st.write(f"👉 {r}")

    # SKILLS
    st.subheader("📚 Recommended Skills to Learn")
    for s in rec_skills:
        st.write(f"👉 {s}")

    # INDUSTRIES
    st.subheader("🏢 Suggested Industries")
    for i in industries:
        st.write(f"👉 {i}")

    # CAREER PATH
    st.subheader("🛤 Detailed Career Path")
    for step in path:
        st.write(f"👉 {step}")

    # COURSES
    st.subheader("🎓 Recommended Courses (Click below)")
    for name, link in courses:
        st.markdown(f"- [{name}]({link})")

    # ================= EXTRA ================= #

    st.subheader("📌 Summary")

    st.info(f"""
    Based on your interest in **{interest}**, you should focus on:
    
    - Building strong projects
    - Improving your resume
    - Learning in-demand skills
    - Applying consistently for internships/jobs
    """)
