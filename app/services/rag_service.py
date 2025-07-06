from langchain.chains import RetrievalQAWithSourcesChain
from langchain.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from app.services.utils import PromptPrinterCallback
from app.services.config import LLM_MODEL, TEMPERATURE
from app.services.vectordb_service import load_vectorstore

import os


def get_qa_chain(vectordb=None):
    if vectordb is None:
        vectordb = load_vectorstore()
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})

    prompt_template = """
    You are a helpful medical assistant with expertise in clinical healthcare. Use only the information from the context below to answer the question. Do not rely on external knowledge.

    Each document in the context is in the format:  
    Content: [text]  
    Source: [filename]

    Instructions:
    - Ignore any in-text citations within the Content (e.g., [1], [PubMed:...], etc.).
    - Assign new citation numbers based on the **unique Source filename**, in the order each source is first used.
    - If the same Source appears multiple times in the context, treat it as **a single source** with one citation number.
    - Do not assign multiple citation numbers to the same file.
    - Summarize in your own words unless a direct quote is necessary.

    Output Format:
    - Write a multi-paragraph answer.
    - Each paragraph must include at least one citation, in square brackets like [1], [2], or [1,3].
    - If a paragraph uses information from only one source (even if it appeared multiple times), cite it with a single number (e.g., [1], not [1,2,3]).
    - You **must** include a **#### Sources** section at the end. This section **must** list only the documents actually cited in the answer, numbered in the exact order the sources were first referenced. If this section is missing, the response is considered incomplete.
    - List each source **only once**, with the number it was first assigned.

    ---

    ### Context:
    {context}

    ### Question:
    {question}

    ### Answer:
    """

    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]
    )

    llm_with_callback = ChatGoogleGenerativeAI(
        model=LLM_MODEL,
        temperature=TEMPERATURE,
        callbacks=[PromptPrinterCallback()],
        google_api_key=os.getenv("GOOGLE_API_KEY"),
    )

    chain = RetrievalQAWithSourcesChain.from_chain_type(
        llm=llm_with_callback,
        chain_type="stuff",
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt, "document_variable_name": "context"},
    )

    return chain
