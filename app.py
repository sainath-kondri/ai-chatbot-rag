import streamlit as st
from rag_pipeline import extract_text_from_pdfs, build_vector_store, create_conversation_chain

# Page config
st.set_page_config(
    page_title="AI Chatbot with RAG",
    page_icon="🤖",
    layout="wide"
)

# Custom CSS
st.markdown("""
    <style>
    .main { background-color: #f5f7fa; }
    .stChatMessage { border-radius: 12px; margin-bottom: 10px; }
    .stButton>button {
        background-color: #0a66c2;
        color: white;
        border-radius: 8px;
        padding: 0.5em 1.5em;
        font-weight: bold;
        border: none;
    }
    .stButton>button:hover { background-color: #084e96; }
    .title-text {
        font-size: 2.2em;
        font-weight: 800;
        color: #0a66c2;
    }
    .subtitle-text {
        font-size: 1em;
        color: #555;
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown('<div class="title-text">🤖 AI Chatbot with RAG</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Upload your PDF documents and chat with them using AI — powered by LangChain + Groq + FAISS</div>', unsafe_allow_html=True)
st.divider()

# Sidebar
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/bot.png", width=80)
    st.markdown("### 📄 Upload Documents")
    uploaded_files = st.file_uploader(
        "Upload one or more PDF files",
        type=["pdf"],
        accept_multiple_files=True
    )

    if st.button("🚀 Process Documents"):
        if uploaded_files:
            with st.spinner("Reading and indexing your documents..."):
                raw_text = extract_text_from_pdfs(uploaded_files)
                vector_store = build_vector_store(raw_text)
                st.session_state.conversation = create_conversation_chain(vector_store)
                st.session_state.chat_history = []
                st.success(f"✅ {len(uploaded_files)} document(s) processed!")
        else:
            st.warning("Please upload at least one PDF file.")

    st.divider()
    st.markdown("### ℹ️ How to Use")
    st.markdown("""
    1. Upload one or more **PDF files**
    2. Click **Process Documents**
    3. Ask any question about the content
    4. Get instant AI-powered answers!
    """)
    st.divider()
    st.markdown("**Built by:** Sainath Kondri")
    st.markdown("**Stack:** LangChain · Groq · FAISS · Streamlit")

# Chat area
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "conversation" not in st.session_state:
    st.session_state.conversation = None

# Display chat history
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
if prompt := st.chat_input("Ask a question about your documents..."):
    if st.session_state.conversation is None:
        st.warning("⚠️ Please upload and process your PDF documents first!")
    else:
        # Show user message
        st.session_state.chat_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)

        # Get AI response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = st.session_state.conversation({"question": prompt})
                answer = response["answer"]
                st.write(answer)
                st.session_state.chat_history.append({"role": "assistant", "content": answer})
