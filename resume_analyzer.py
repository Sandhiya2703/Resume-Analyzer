import streamlit as st
import pandas as pd
import fitz  # PyMuPDF
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from fpdf import FPDF
import os
import datetime
import re

# 🔷 Gradient background function
def set_gradient_background():
    st.markdown(
        """
        <style>
        .stApp {
            background: linear-gradient(120deg, #fdfbfb 0%, #ebedee 100%);
            background-attachment: fixed;
            font-family: 'Segoe UI', sans-serif;
        }

        .block-container {
            background-color: rgba(255, 255, 255, 0.8);
            padding: 2rem 2rem 2rem 2rem;
            border-radius: 15px;
            box-shadow: 0px 0px 10px rgba(0,0,0,0.1);
        }

        h1, h2, h3, h4, h5 {
            color: #2c3e50;
        }

        .stButton > button {
            background-color: #00bfa5;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5rem 1rem;
        }

        .stDownloadButton > button {
            background-color: #009688;
            color: white;
            font-weight: bold;
            border-radius: 8px;
            padding: 0.5rem 1rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )




# 🔍 Load job description keywords
def load_job_keywords(job_role):
    try:
        with open(f"job_descriptions/{job_role}.txt", "r") as f:
            keywords = f.read().splitlines()
        return " ".join(keywords)
    except FileNotFoundError:
        st.error("Job role not found. Please upload correct files.")
        return ""

# 📄 Extract text from PDF
def extract_text_from_pdf(pdf_file):
    text = ""
    with fitz.open(stream=pdf_file.read(), filetype="pdf") as doc:
        for page in doc:
            text += page.get_text()
    return text

# 📊 Analyze resume and score
def analyze_resume(resume_text, job_keywords):
    cv = CountVectorizer().fit_transform([resume_text, job_keywords])
    score = cosine_similarity(cv[0:1], cv[1:2])[0][0]
    return round(score * 100, 2)

# ❌ Get missing skills
def get_missing_skills(resume_text, job_keywords):
    resume_words = set(resume_text.lower().split())
    job_words = set(job_keywords.lower().split())
    missing_skills = job_words - resume_words
    return list(missing_skills)

# 🎯 Highlight resume skills
def highlight_resume_text(resume_text, job_keywords):
    resume_lower = resume_text.lower()
    keywords = job_keywords.lower().split()
    for word in keywords:
        if word in resume_lower:
            resume_text = re.sub(f"(?i)\\b{re.escape(word)}\\b", f"🟩**{word}**", resume_text)
        else:
            resume_text = re.sub(f"(?i)\\b{re.escape(word)}\\b", f"🟥**{word}**", resume_text)
    return resume_text

# 📈 Plot matched/unmatched skill charts
def plot_skill_match(resume_text, job_keywords):
    resume_words = resume_text.lower().split()
    job_words = job_keywords.lower().split()
    matched = [word for word in job_words if word in resume_words]
    unmatched = [word for word in job_words if word not in resume_words]

    matched_count = len(matched)
    unmatched_count = len(unmatched)

    # Bar chart
    fig1, ax1 = plt.subplots()
    ax1.bar(["Matched Skills", "Unmatched Skills"], [matched_count, unmatched_count], color=['green', 'red'])
    ax1.set_title("Resume Skill Match (Bar)")
    ax1.set_ylabel("Skill Count")
    st.pyplot(fig1)

    # Pie chart
    fig2, ax2 = plt.subplots()
    ax2.pie([matched_count, unmatched_count],
            labels=["Matched", "Unmatched"],
            colors=["green", "red"],
            autopct='%1.1f%%',
            startangle=140)
    ax2.set_title("Resume Skill Distribution (Pie)")
    ax2.axis('equal')
    st.pyplot(fig2)

    # Summary
    st.write(f"✅ Matched: {matched_count} skills")
    st.write(f"❌ Unmatched: {unmatched_count} skills")

# 📝 Generate PDF feedback
def generate_feedback_report(score, missing_skills, job_role):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt="AI Resume Analyzer Report", ln=1, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, txt=f"Job Role: {job_role}", ln=1)
    pdf.cell(200, 10, txt=f"Matching Score: {score}/100", ln=1)
    pdf.ln(5)
    pdf.cell(200, 10, txt="Missing Skills:", ln=1)
    for skill in missing_skills:
        pdf.cell(200, 8, txt=f"- {skill}", ln=1)

    now = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"resume_feedback_{now}.pdf"
    pdf.output(filename)
    return filename

# 🚀 Streamlit app
def main():
    st.set_page_config(page_title="AI Resume Analyzer", layout="centered")
    set_gradient_background()
    st.title("📄 AI Resume Analyzer")
    st.write("Upload one or more resumes (PDF) and select a job role to match.")

    job_files = os.listdir("job_descriptions")
    job_roles = [f.replace(".txt", "") for f in job_files if f.endswith(".txt")]

    job_role = st.selectbox("Select Job Role", job_roles)
    uploaded_files = st.file_uploader("Upload Resume(s)", type=["pdf"], accept_multiple_files=True)

    if uploaded_files and job_role:
        job_keywords = load_job_keywords(job_role)

        if job_keywords:
            candidate_scores = []

            for i, uploaded_file in enumerate(uploaded_files, start=1):
                resume_text = extract_text_from_pdf(uploaded_file)
                score = analyze_resume(resume_text, job_keywords)
                missing_skills = get_missing_skills(resume_text, job_keywords)

                candidate_scores.append({
                    "name": uploaded_file.name,
                    "score": score,
                    "resume_text": resume_text,
                    "missing_skills": missing_skills,
                    "file": uploaded_file
                })

            # Sort by best score
            candidate_scores.sort(key=lambda x: x["score"], reverse=True)
            best_candidate = candidate_scores[0]
            st.markdown(f"## 🏆 Best Candidate: `{best_candidate['name']}` with **{best_candidate['score']} / 100**")

            for i, candidate in enumerate(candidate_scores, start=1):
                st.markdown(f"---\n### 📌 Candidate {i}: `{candidate['name']}`")
                st.write(f"✅ **Matching Score:** {candidate['score']} / 100")

                # ✅ Eligibility check
                resume_words = candidate["resume_text"].lower().split()
                job_words = job_keywords.lower().split()
                matched = [word for word in job_words if word in resume_words]
                match_percentage = (len(matched) / len(job_words)) * 100

                if match_percentage >= 60:
                    st.success(f"✅ Eligible: Good match ({match_percentage:.1f}% skills matched)")
                else:
                    st.warning(f"⚠️ Not Eligible: Only {match_percentage:.1f}% of skills matched")

                st.subheader("📋 Missing Skills")
                if candidate["missing_skills"]:
                    st.write(", ".join(candidate["missing_skills"]))
                else:
                    st.write("✅ No major skills missing!")

                st.subheader("📊 Skill Match Chart")
                plot_skill_match(candidate["resume_text"], job_keywords)

                with st.expander("📄 View Resume Text with Highlights"):
                    highlighted_text = highlight_resume_text(candidate["resume_text"], job_keywords)
                    st.markdown(highlighted_text, unsafe_allow_html=True)

                if st.button(f"📥 Download Feedback Report for {candidate['name']}", key=f"download_{i}"):
                    pdf_file = generate_feedback_report(candidate["score"], candidate["missing_skills"], job_role)
                    with open(pdf_file, "rb") as f:
                        st.download_button("Download Report", f, file_name=pdf_file, key=f"btn_{i}")

if __name__ == "__main__":
    main()

#how to run using this comment......streamlit run resume_analyzer.py 