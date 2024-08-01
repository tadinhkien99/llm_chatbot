#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    app.py
# @Author:      Kuro
# @Time:        7/30/2024 11:41 PM
import uvicorn
from elasticsearch import Elasticsearch
from fastapi import FastAPI

from controllers.chatbot_controller import ChatbotController
from embeddings.elastic.config import ElasticConfig
from services.embedding_service import EmbeddingService

app = FastAPI()

client = Elasticsearch(
    hosts=ElasticConfig.hosts,
    # api_key=self.config.api_key,
    verify_certs=False, request_timeout=10000
)
document_service = EmbeddingService(client)
document_service.load_data(data_path="dataset")

chatbot = ChatbotController(client)


@app.post("/chat")
async def chat(user_query: str):
    response = chatbot.handle_chat(user_query)
    return {"response": response}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8020)
