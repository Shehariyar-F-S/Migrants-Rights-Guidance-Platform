import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

DATA_DIR = "data"              # folder with all your PDFs
CHROMA_DIR = "dublin_chroma"   # same as before

# 1) Collect documents from all PDFs
all_docs = []
for filename in os.listdir(DATA_DIR):
    if not filename.lower().endswith(".pdf"):
        continue
    pdf_path = os.path.join(DATA_DIR, filename)
    print(f"Loading {pdf_path} ...")

    loader = PyPDFLoader(pdf_path)
    docs = loader.load()

    # optional: add a source field so you know which file a chunk came from
    for d in docs:
        d.metadata = d.metadata or {}
        d.metadata["source"] = filename

    all_docs.extend(docs)

print(f"Loaded {len(all_docs)} documents from PDFs in {DATA_DIR}")

# 2) Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
)
chunks = splitter.split_documents(all_docs)
print(f"Created {len(chunks)} chunks")

# 3) Embeddings model (local)
embedding_fn = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# 4) Create / persist vector store with all chunks
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_fn,
    persist_directory=CHROMA_DIR,
)
vectordb.persist()
print(f"Indexed chunks into {CHROMA_DIR}")
