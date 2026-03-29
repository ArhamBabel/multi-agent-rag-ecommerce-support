import os 
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings


def load_documents(data_path="data"):
    documents = []
    for file in os.listdir(data_path):
        if file.endswith(".txt"):
            loader = TextLoader(os.path.join(data_path, file))
            documents.extend(loader.load())

    return documents

def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size =300,
        chunk_overlap = 50
    )

    chunks = splitter.split_documents(documents)
    return chunks

def create_vectorstore(chunks):
    embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
   )  
    vectorstore = FAISS.from_documents(chunks, embeddings)
    vectorstore.save_local("vectorstore")
    return vectorstore

if __name__ == "__main__":
    docs = load_documents()
    chunks = split_documents(docs)
    create_vectorstore(chunks)
    print("✅ Vector store created successfully!")
