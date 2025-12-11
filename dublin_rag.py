# dublin_rag.py
from langchain_community.llms import Ollama
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings

# Reload vector store
embedding_fn = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = Chroma(
    embedding_function=embedding_fn,
    persist_directory="dublin_chroma"
)
retriever = vectordb.as_retriever(search_kwargs={"k": 4})

# Llama 3 via Ollama
llm = Ollama(model="llama3")

template = """
You are a legal assistant answering questions only from the provided context about the Dublin Regulation.
If the answer is not in the context, say you don't know.

Question:
{question}

Context:
{context}

Answer in a concise paragraph.
"""
prompt = PromptTemplate(input_variables=["question", "context"], template=template)

def rag_answer(question: str) -> str:
    docs = retriever.invoke(question)
    context = "\n\n".join(d.page_content for d in docs)
    full_prompt = prompt.format(question=question, context=context)
    return llm.invoke(full_prompt)
