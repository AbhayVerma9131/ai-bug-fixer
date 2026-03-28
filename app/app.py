import streamlit as st
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.ai_engine import fix_bug

st.set_page_config(page_title="AI Bug Fixer")

st.title("🐞 AI Bug Fixer")

code = st.text_area("Paste your buggy code here", height=200)

if st.button("Fix Bug"):
    if code:
        with st.spinner("Analyzing and fixing..."):
            result = fix_bug(code)

        st.subheader("🔍 Analysis & Fix")
        st.write(result)
