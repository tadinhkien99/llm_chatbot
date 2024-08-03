#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    app.py
# @Author:      Kuro
# @Time:        7/30/2024 11:41 PM

import uvicorn
from elasticsearch import Elasticsearch
from fastapi import FastAPI
from openai import OpenAI

from controllers.chatbot_controller import ChatbotController
from embeddings.elastic.config import ElasticConfig
from models.openAI_model.config import OpenAIConfig
from services.embedding_service import EmbeddingService

app = FastAPI()

embedding_client = Elasticsearch(
    hosts=ElasticConfig.hosts,
    api_key=ElasticConfig.api_key,
    verify_certs=False, request_timeout=30
)
openai_client = OpenAI(api_key=OpenAIConfig.openai_api_key)
document_service = EmbeddingService(embedding_client, openai_client)
document_service.load_data(data_path="dataset")

chatbot = ChatbotController(embedding_client, openai_client)


@app.post("/chat")
async def chat(user_query: str):
    response = chatbot.handle_chat(user_query)
    return {"response": response}


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8020)
