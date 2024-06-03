from pydantic import BaseModel
from fastapi import FastAPI
from retrievalChroma import retreival_response
from retrievalFaiss import user_input


app = FastAPI()

class QueryRequest(BaseModel):
    query: str
    Key:str

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.post("/faiss")
async def read_item(query_request: QueryRequest):
    query = query_request.query
    key = query_request.Key
    print(query_request)
    res = user_input(query, "faiss_db", key)
    return {"Query": query, "Database": "Faiss", "Result": res}

@app.post("/chroma")
async def read_item(query_request: QueryRequest):
    query = query_request.query
    key = query_request.Key
    res = retreival_response("chroma_db", "harsh", query,  key)
    return {"Query": query, "Database": "ChromaDb", "Result": res}
