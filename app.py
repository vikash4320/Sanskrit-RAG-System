from loader import load_documents
from preprocess import split_documents
from embeddings import get_embeddings
from vectorstore import build_vectorstore
from rag_pipeline import generate_answer

docs = load_documents("data/sample_sanskrit.txt")
chunks = split_documents(docs)
vectorstore = build_vectorstore(chunks, get_embeddings())
retriever = vectorstore.as_retriever()

while True:
    q = input("Enter Sanskrit Query: ")
    if q.lower() == "exit":
        break
    print("🟢 उत्तर:", generate_answer(q, retriever))
