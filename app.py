import streamlit as st

from summarizer import summarize_text

st.set_page_config(
    page_title="AI Auto Summarizer",
    page_icon="📝",
    layout="wide"
)

st.title("📝 AI Auto Summarizer")
st.write("Paste any long text and get an AI-generated summary in seconds.")

text = st.text_area(
    "Paste your text here",
    height=300,
    placeholder="Paste an article, blog, notes, research paper..."
)

word_count = len(text.split())
character_count = len(text)
reading_time = max(1, word_count // 200)

col1, col2, col3 = st.columns(3)

col1.metric("Words", word_count)
col2.metric("Characters", character_count)
col3.metric("Reading Time", f"{reading_time} min")

if st.button("Summarize"):

    if not text.strip():
        st.warning("Please paste some text first.")

    else:
        with st.spinner("Summarizing..."):

            summary = summarize_text(text)

        st.success("Summary Generated!")

        st.markdown(summary)