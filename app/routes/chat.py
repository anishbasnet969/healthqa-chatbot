from fastapi import APIRouter, Body
from fastapi.responses import JSONResponse
from app.services import rag_service, vectordb_service

router = APIRouter()


@router.post("/")
async def chat(message: str = Body(..., embed=True)):
    if not message:
        return JSONResponse(content={"error": "No message provided."}, status_code=400)

    try:
        vectordb = vectordb_service.load_vectorstore()
    except Exception as e:
        print("Failed to load vectorstore, creating a new one. ", e)
        vectordb = vectordb_service.get_vectorstore()

    chain = rag_service.get_qa_chain(vectordb)
    result = chain.invoke({"question": message})

    answer = result.get("answer", "No answer generated.")
    source_documents = result.get("source_documents", [])

    source_info = []
    for doc in source_documents:
        source_info.append(
            {
                "content": (
                    doc.page_content[:200] + "..."
                    if len(doc.page_content) > 200
                    else doc.page_content
                ),
                "source": doc.metadata.get("source", "Unknown"),
                "page": doc.metadata.get("page", "Unknown"),
            }
        )

    response = {
        "answer": answer,
        "source_documents": source_info,
    }

    return JSONResponse(content=response)
