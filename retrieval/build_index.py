import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from vectorstore import save_vectorstore
from langchain_community.embeddings import HuggingFaceEmbeddings

PDF_FOLDER = "data/pitch_docs"

def load_documents():
    docs = []
    for file in os.listdir(PDF_FOLDER):
        if file.endswith(".pdf"):
            loader = PyPDFLoader(os.path.join(PDF_FOLDER, file))
            loaded_docs = loader.load()
            for doc in loaded_docs:
                doc.metadata["source"] = file
            docs.extend(loaded_docs)
    return docs

def chunk_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=100,
    )
    return splitter.split_documents(documents)

def build_index():
    print("Loading PDFs...")
    docs = load_documents()

    print("Chunking documents...")
    chunks = chunk_documents(docs)

    print("Creating embeddings...")
    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )   

    print("Building FAISS index...")
    vectorstore = FAISS.from_documents(chunks, embeddings)

    print("Saving index...")
    save_vectorstore(vectorstore)

    print("Index built successfully.")

if __name__ == "__main__":
    build_index()