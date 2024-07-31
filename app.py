#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    app.py
# @Author:      Kuro
# @Time:        7/30/2024 11:41 PM
from fastapi import FastAPI

from controllers import chatbot_controller
from embeddings.elastic.database import EmbeddingDatabase
from services.document_service import DocumentService

app = FastAPI()

db = EmbeddingDatabase()
document_service = DocumentService(data_path="dataset")

db.create_index()
document_service.load_data(data_path="dataset")


@app.post("/chat")
async def chat(user_query: str):
    response = chatbot_controller.handle_chat(user_query)
    return {"response": response}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8020)
