import streamlit as st
from resumeparser import parse_resume
from similaritymodel import compute_similarity


def main():
    st.title("🧠 AI Resume Screening App")

    st.write("Upload a résumé and a job description to check how well they match!")

    job_description = st.text_area("📄 Enter Job Description")

    uploaded_file = st.file_uploader(
        "📎 Upload Résumé", type=["pdf", "docx" ]
    )

    if uploaded_file and job_description.strip():
        st.info("Processing résumé... please wait.")

        resume_text = parse_resume(uploaded_file)
        score = compute_similarity(job_description, resume_text)

        st.subheader(f"✅ Match Score: {score:.2f}%")

        if score >= 70:
            st.success("🟢 Shortlisted")
        elif score >= 50:
            st.warning("🟡 Consider")
        else:
            st.error("🔴 Not Suitable")

        with st.expander("🔍 View Extracted Résumé Text"):
            st.write(resume_text)
    else:
        st.warning("Please upload a résumé and provide a job description.")


if __name__ == "__main__":
    main()
