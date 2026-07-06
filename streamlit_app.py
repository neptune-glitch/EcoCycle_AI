import tempfile
import streamlit as st

from skills.identify import identify
from skills.retrieve import retrieve
from skills.advise import advise
from skills.security import security_check

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------
st.set_page_config(
    page_title="EcoCycle AI",
    page_icon="♻️",
    layout="wide"
)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
with st.sidebar:
    st.title("♻️ EcoCycle AI")
    st.write(
        """
        This AI agent can:

        ✅ Identify waste from a photo\n
        ✅ Search a recycling knowledge base (RAG)\n
        ✅ Generate AI-written reuse & upcycling ideas\n
        ✅ Filter unsafe/malicious input before it reaches the agent\n
        """
    )
    st.markdown("---")
    st.caption("Built for Earth 🌍 · Gemini 2.5 Flash · ChromaDB · ADK")

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------
st.markdown(
    """
    # ♻️ EcoCycle AI
    ### Smart Waste Identification & AI Reuse-Hack Generator

    Upload any waste image and get an AI-generated recycling &
    reuse plan — not just a lookup.
    """
)

st.markdown("---")

# ---------------------------------------------------
# OPTIONAL: user note / context (also demonstrates the security agent tool)
# ---------------------------------------------------
user_note = st.text_input(
    "Optional: add a note about this item (e.g. 'it's a bit dirty')",
    ""
)

if user_note:
    check = security_check(user_note)
    if check == "BLOCKED":
        st.error("🔒 That note was blocked by the security filter for containing unsafe content.")
        st.stop()
    else:
        st.caption("🔒 Security check passed — note will be used as extra context.")

# ---------------------------------------------------
# UPLOAD SECTION
# ---------------------------------------------------
uploaded_file = st.file_uploader(
    "📤 Upload a waste image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file:

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:
        tmp.write(uploaded_file.read())
        image_path = tmp.name

    try:
        with st.spinner("🔍 AI is identifying your item..."):
            item = identify(image_path)

        with st.spinner("♻️ Searching recycling knowledge base..."):
            knowledge = retrieve(item)

        with st.spinner("🤖 AI is generating your reuse plan..."):
            answer = advise(item, knowledge)

    except Exception as e:
        error_text = str(e).lower()

        if any(keyword in error_text for keyword in
               ["quota", "rate limit", "429", "resourceexhausted", "resource_exhausted"]):
            st.error("🚦 We've hit the AI usage limit for now.")
            st.warning(
                "The Gemini API free-tier quota has been reached. "
                "This usually resets after a short while. Please try again shortly 🙏"
            )
        else:
            st.error("⚠️ Something went wrong while processing your image.")
            st.warning("Please try again, or upload a different image.")

        with st.expander("🔧 Technical details (for developers)"):
            st.code(str(e))

        st.stop()

    st.markdown("## 🔎 Results")

    col1, col2 = st.columns([1, 1])

    with col1:
        st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    with col2:
        st.metric(label="🧠 Detected Waste", value=item)
        st.success("✅ AI reuse plan generated below")

    st.markdown("---")
    st.markdown("## ♻️ AI-Generated Recycling & Reuse Plan")
    st.markdown(answer)

    with st.expander("📖 View Raw Knowledge Base Match (RAG source)"):
        st.write(knowledge)

    st.markdown("---")
    st.markdown(
        """
        ### 🌱 Every small action counts
        Recycling this item helps reduce landfill waste and supports a cleaner planet.
        """
    )

else:
    st.info("👆 Upload a waste image above to get started.")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------
st.markdown("---")
st.caption("Made with ❤️ using Gemini API • ChromaDB • Google ADK • Streamlit")