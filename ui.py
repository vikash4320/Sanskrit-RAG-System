import streamlit as st
from loader import load_documents
from preprocess import split_documents
from embeddings import get_embeddings
from vectorstore import build_vectorstore
from rag_pipeline import generate_answer

# --- Load documents and setup retriever ---
@st.cache_data(show_spinner=True)
def setup_pipeline():
    docs = load_documents("data/sample_sanskrit.txt")
    chunks = split_documents(docs)
    embeddings = get_embeddings()
    vectorstore = build_vectorstore(chunks, embeddings)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 5})
    return retriever

retriever = setup_pipeline()

# --- Streamlit UI ---
st.title("Sanskrit RAG System")
st.write("Type your Sanskrit query below and press Enter or Submit")

query = st.text_input("Enter Sanskrit Query:")

if query:
    with st.spinner("Generating answer..."):
        answer = generate_answer(query, retriever)

    st.markdown(f"🟢 **उत्तर:** {answer}")
