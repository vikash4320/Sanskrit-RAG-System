import unicodedata
from langchain_text_splitters import RecursiveCharacterTextSplitter

def normalize_text(text):
    return unicodedata.normalize("NFC", text)

from langchain_text_splitters import RecursiveCharacterTextSplitter

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=300,
        chunk_overlap=50,
        separators=["\n\n", "\n", "।", " ", ""]
    )
    return splitter.split_documents(documents)

