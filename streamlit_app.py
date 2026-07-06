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
# CUSTOM CSS
# ---------------------------------------------------
st.markdown("""
<style>

.main {
    padding-top:1rem;
}

div[data-testid="stMetric"]{
    background-color:#f8f9fa;
    border-radius:12px;
    padding:15px;
    border:1px solid #e6e6e6;
}

div.stButton>button{
    border-radius:10px;
}

</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------
# SIDEBAR
# ---------------------------------------------------
with st.sidebar:

    st.image("https://img.icons8.com/color/96/recycle.png", width=70)

    st.title("EcoCycle AI")

    st.markdown("### 🌍 About")

    st.write(
        """
EcoCycle AI uses **Gemini Vision + ChromaDB RAG**
to identify waste and provide sustainable recycling
recommendations.
"""
    )

    st.markdown("---")

    st.markdown("### ✅ Supported Waste")

    st.markdown("""
- Plastic Bottle
- Glass Bottle
- Plastic Bag
- Tin Can
- Aluminum Can
- Newspaper
- Cardboard
- Banana Peel
- Coffee Grounds
- Egg Shell
""")

    st.markdown("---")

    st.success("🌱 Every recycled item makes a difference!")

# ---------------------------------------------------
# HERO
# ---------------------------------------------------

st.title("♻️ EcoCycle AI")

st.subheader("Smart Waste Identification & Recycling Assistant")

st.write(
"""
Upload a waste image and EcoCycle AI will:

✅ Identify the waste item

♻️ Search an AI-powered recycling knowledge base

🌱 Generate reuse ideas

💚 Give eco-friendly recycling advice
"""
)

st.divider()

# ---------------------------------------------------
# USER NOTE
# ---------------------------------------------------

user_note = st.text_input(
    "💬 Optional Note",
    placeholder="Example: The bottle still has some liquid inside."
)

if user_note:

    check = security_check(user_note)

    if check == "BLOCKED":

        st.error("🚫 Unsafe content detected.")

        st.stop()

    st.success("🔒 Security check passed.")

# ---------------------------------------------------
# FILE UPLOAD
# ---------------------------------------------------

uploaded_file = st.file_uploader(
    "📷 Upload Waste Image",
    type=["jpg","jpeg","png"]
)

# ---------------------------------------------------
# MAIN
# ---------------------------------------------------

if uploaded_file:

    st.divider()

    with tempfile.NamedTemporaryFile(delete=False, suffix=".jpg") as tmp:

        tmp.write(uploaded_file.read())

        image_path = tmp.name

    progress = st.progress(0)

    try:

        progress.progress(20)

        with st.spinner("🧠 Identifying waste..."):
            item = identify(image_path)

        progress.progress(45)

        with st.spinner("♻️ Searching knowledge base..."):
            knowledge = retrieve(item)

        progress.progress(75)

        with st.spinner("🤖 Generating recycling advice..."):
            answer = advise(item, knowledge)

        progress.progress(100)

    except Exception as e:

        txt = str(e).lower()

        if any(x in txt for x in ["429","quota","resource_exhausted"]):

            st.error("🚦 Gemini API quota exceeded.")

            st.info("Please wait a while and try again.")

        else:

            st.error("⚠️ Something went wrong.")

            with st.expander("Technical Details"):
                st.code(str(e))

        st.stop()

    # --------------------------------------------

    col1,col2 = st.columns([1,1])

    with col1:

        st.image(
            uploaded_file,
            caption="Uploaded Image",
            use_container_width=True
        )

    with col2:

        st.metric("🧠 Detected Waste", item)

        st.success("AI analysis completed successfully.")

        st.info("The recycling information below comes from the AI knowledge base.")

    st.divider()

    st.subheader("♻️ Recycling Recommendation")

    with st.container(border=True):

        st.markdown(answer)

    st.divider()

    with st.expander("📖 View Knowledge Base Match"):

        st.code(knowledge)

    st.divider()

    st.success(
        "🌍 Great job! Recycling this item helps reduce landfill waste and protects the environment."
    )

else:

    st.info("👆 Upload a waste image to begin.")

# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.divider()

st.caption(
    "Made with ❤️ using Gemini 2.5 Flash • ChromaDB • Streamlit • Google ADK"
)