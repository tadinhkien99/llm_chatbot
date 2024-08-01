#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    chatbot_service.py
# @Author:      Kuro
# @Time:        7/31/2024 9:28 PM


import openai

from embeddings.create_embedding import OpenAIEmbedding
from embeddings.elastic.database import EmbeddingDatabase
from models.openAI_model.config import OpenAIConfig


class ChatbotService:
    def __init__(self, elasticsearch_database: EmbeddingDatabase):
        self.embeddings = OpenAIEmbedding()
        self.elasticsearch_database = elasticsearch_database
        self.openai_config = OpenAIConfig()
        openai.api_key = self.openai_config.openai_api_key

    def get_response(self, user_query: str):
        # Create an embedding from the user query
        query_embedding = self.embeddings.create_embedding(user_query)

        # Retrieve relevant data (dummy example, replace with real retrieval logic)
        retrieved_data = self.retrieve_data(query_embedding)

        # Generate a response using the retrieved data
        message = [
            {"role": "system", "content": "You are a helpful assistant."},
            {
                "role": "user",
                "content": f"""Answer the following input: {user_query} by providing the following response: {retrieved_data}"""
            },
        ]
        response = openai.ChatCompletion.create(model=self.openai_config.model_name, messages=message).choices[0].message.content
        return response

    def retrieve_data(self, query_embedding):
        # Retrieve relevant data based on the query embedding (dummy example, replace with real retrieval logic)
        return self.elasticsearch_database.search(query_embedding)
