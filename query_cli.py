from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import SentenceTransformerEmbeddings
from langchain_community.llms import Ollama
from langchain.prompts import PromptTemplate

CHROMA_DIR = "dublin_chroma"

# 1) Load existing vector store (no PDF loading here)
embedding_fn = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
vectordb = Chroma(
    embedding_function=embedding_fn,
    persist_directory=CHROMA_DIR,
)
retriever = vectordb.as_retriever(search_kwargs={"k": 4})

# 2) LLM + prompt (same as before)
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

if __name__ == "__main__":
    while True:
        q = input("\nYour question (or 'exit'): ")
        if q.lower() in ("exit", "quit"):
            break
        print("\nAnswer:\n")
        print(rag_answer(q))
