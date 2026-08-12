import streamlit as st
import re
import pandas as pd

from pdf_parser import extract_text
from database import (
    create_table,
    insert_candidate,
    get_all_candidates
)

from ai_analyzer import analyze_resume

# Create database table
create_table()

st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI Resume Analyzer")
st.write("Upload a resume and get AI-powered analysis.")

uploaded_file = st.file_uploader(
    "Upload Resume PDF",
    type=["pdf"]
)

if uploaded_file:

    # Extract text from PDF
    text = extract_text(uploaded_file)

    # Extract email
    email_match = re.search(
        r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}',
        text
    )

    email = email_match.group() if email_match else "Not Found"

    # Extract phone number
    phone_match = re.search(
        r'\b\d{10}\b',
        text
    )

    phone = phone_match.group() if phone_match else "Not Found"

    st.subheader("📋 Basic Details")
    st.write("📧 Email:", email)
    st.write("📱 Phone:", phone)

    # AI Analysis
    with st.spinner("Analyzing Resume with AI..."):
        analysis = analyze_resume(text)

    st.subheader("🤖 AI Resume Analysis")
    st.write(analysis)

    # Save Resume
    if st.button("💾 Save Resume"):

        insert_candidate(
            email,
            phone,
            "AI Generated",
            0,
            text
        )

        st.success("Resume saved successfully!")

# Show saved resumes
st.subheader("📂 Stored Resumes")

data = get_all_candidates()

if len(data) > 0:

    df = pd.DataFrame(
        data,
        columns=[
            "ID",
            "Email",
            "Phone",
            "Skills",
            "Score",
            "Resume Text"
        ]
    )

    search = st.text_input(
        "Search by Email"
    )

    if search:
        df = df[
            df["Email"].str.contains(
                search,
                case=False,
                na=False
            )
        ]

    st.dataframe(
        df,
        use_container_width=True
    )

else:
    st.info("No resumes stored yet.")