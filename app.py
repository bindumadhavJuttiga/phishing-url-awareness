
import streamlit as st
from phishing_checker import inspect_url

st.set_page_config(
    page_title="Phishing URL Awareness Checker",
    page_icon="🔐",
    layout="centered"
)

st.title("🔐 Phishing URL Awareness Checker")
st.write(
    "Check URLs for common phishing warning signs "
    "using Python."
)

st.info(
    "This educational tool checks URL text only. "
    "It does not guarantee website safety."
)

url = st.text_input(
    "Enter a URL to check",
    placeholder="https://example.com/login"
)

if st.button("Check URL", type="primary"):
    if not url.strip():
        st.warning("Please enter a URL.")
    else:
        findings = inspect_url(url)

        st.subheader("Analysis Results")

        if findings and findings[0].startswith(
            "No listed warning signs"
        ):
            st.success("No listed warning signs found.")
        elif findings and findings[0].startswith(
            ("No URL entered", "Could not identify",
             "This text is not")
        ):
            st.warning(findings[0])
        else:
            st.warning("Warning signs detected. Review carefully.")

        for finding in findings:
            st.write("⚠️", finding)

        st.caption(
            "No warning signs does not mean a URL is safe."
        )

st.divider()
st.caption("EWB Cybersecurity Internship | Python Project")
