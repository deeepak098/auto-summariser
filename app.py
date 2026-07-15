import streamlit as st
from summarizer import summarize_text

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="AI Auto Summarizer",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown(
    """
<style>

.block-container{
    max-width:1200px;
    padding-top:2rem;
    padding-bottom:2rem;
}

.main-title{
    text-align:center;
    font-size:3rem;
    font-weight:700;
    margin-bottom:0;
}

.subtitle{
    text-align:center;
    color:#6b7280;
    font-size:1.05rem;
    margin-top:0;
    margin-bottom:2rem;
}

.info-card{
    border:1px solid rgba(128,128,128,.2);
    border-radius:14px;
    padding:18px;
    background:rgba(255,255,255,.03);
}

.output-card{
    border:1px solid rgba(128,128,128,.2);
    border-radius:14px;
    padding:22px;
    background:rgba(255,255,255,.03);
}

.stButton > button{
    width:100%;
    height:55px;
    font-size:18px;
    font-weight:600;
    border-radius:12px;
}

</style>
""",
    unsafe_allow_html=True,
)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    """
<div class="main-title">📝 AI Auto Summarizer</div>

<div class="subtitle">
Summarize long articles, blogs, reports and notes using Groq AI.
</div>
""",
    unsafe_allow_html=True,
)

st.divider()

# ---------------------------------------------------
# LAYOUT
# ---------------------------------------------------

left_col, right_col = st.columns([3, 1])

# ---------------- LEFT ----------------

with left_col:

    text = st.text_area(
        "📄 Paste your text",
        height=420,
        placeholder="Paste any article, blog, research paper or notes here...",
    )

# ---------------- RIGHT ----------------

with right_col:

    word_count = len(text.split())
    character_count = len(text)

    reading_time = max(1, round(word_count / 200))

    st.markdown(
        '<div class="info-card">',
        unsafe_allow_html=True,
    )

    st.subheader("📊 Statistics")

    st.metric("Words", word_count)

    st.metric("Characters", character_count)

    st.metric("Reading Time", f"{reading_time} min")

    st.markdown("</div>", unsafe_allow_html=True)

    st.write("")

    st.info(
        """
💡 **Tips**

• Paste long text

• Works best with 200+ words

• Generates 3 sentence summary

• Extracts 5 key takeaways
"""
    )

st.write("")

# ---------------------------------------------------
# BUTTON
# ---------------------------------------------------

generate = st.button(
    "🚀 Generate Summary",
    use_container_width=True,
)

# ---------------------------------------------------
# GENERATE
# ---------------------------------------------------

if generate:

    if not text.strip():

        st.warning("Please paste some text before generating a summary.")

    else:

        with st.spinner("Generating summary..."):

            summary = summarize_text(text)

        st.toast("Summary generated successfully!")

        st.success("Done!")

        st.divider()

        st.subheader("✨ AI Generated Summary")

        # Theme-safe container
        with st.container(border=True):
            st.markdown(summary)

        st.write("")

        st.download_button(
            label="📥 Download Summary",
            data=summary,
            file_name="summary.txt",
            mime="text/plain",
            use_container_width=True,
        )

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------

with st.sidebar:

    st.title("📝 About")

    st.write(
        """
This project uses:

- ⚡ Streamlit
- 🤖 Groq API
- 🦙 Llama 3.3 70B
"""
    )

    st.divider()

    st.write("### Workflow")

    st.write(
        """
1. Paste text

2. Click **Generate Summary**

3. AI processes your input

4. Get:
- 3 sentence summary
- 5 key takeaways
"""
    )

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()

st.caption("Built with ❤️ using Streamlit + Groq")