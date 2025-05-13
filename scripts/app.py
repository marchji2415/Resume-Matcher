import streamlit as st  # type: ignore
from scripts import ResumeProcessor, JobDescriptionProcessor  # adjust if needed

st.title("Resume Matcher")

resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx"])
jd_file = st.file_uploader("Upload Job Description", type=["pdf", "docx"])

if resume_file and jd_file:
    with st.spinner("Parsing documents..."):

        # Save temporarily to disk
        with open("temp_resume.pdf", "wb") as f:
            f.write(resume_file.read())
        with open("temp_jd.pdf", "wb") as f:
            f.write(jd_file.read())

        # Parse using your existing classes
        resume_data = ResumeProcessor("temp_resume.pdf").process()
        jd_data = JobDescriptionProcessor("temp_jd.pdf").process()

    st.success("Parsing Complete!")

    # Show raw parsed output
    st.subheader("Parsed Resume Data")
    st.json(resume_data)

    st.subheader("Parsed Job Description Data")
    st.json(jd_data)

    # You can add matching logic here too
