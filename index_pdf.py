from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

PDF_PATH = "DUBLIN REGULATIONS.pdf"

# 1) Load PDF
loader = PyPDFLoader(PDF_PATH)
docs = loader.load()

# 2) Split into chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200
)
chunks = splitter.split_documents(docs)

# 3) Embeddings model (local)
embedding_fn = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

# 4) Create / persist vector store
vectordb = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_fn,
    persist_directory="dublin_chroma"
)
vectordb.persist()
