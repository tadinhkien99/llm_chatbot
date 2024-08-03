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
    def __init__(self, elasticsearch_database: EmbeddingDatabase, openai_client: openai.OpenAI):
        self.embeddings = OpenAIEmbedding(openai_client)
        self.elasticsearch_database = elasticsearch_database
        self.openai_client = openai_client
        self.openai_config = OpenAIConfig()
        with open("models/openAI_model/whole_short_response.txt", "r") as f:
            self.system_prompt = f.read()

    def get_response(self, user_query: str):
        # Create an embedding from the user query
        query_embedding = self.embeddings.create_embedding(user_query)

        # Retrieve relevant data (dummy example, replace with real retrieval logic)
        retrieved_data = self.retrieve_data(query_embedding)
        retrieved_data = retrieved_data[0]['_source']['text'] if retrieved_data else "No data found."
        # Generate a response using the retrieved data
        message = [
            {"role": "system", "content": f"{self.system_prompt}"},
            {
                "role": "user",
                "content": f"""Answer the following input: {user_query} by providing the following response: {retrieved_data}"""
            },
        ]
        response = self.openai_client.chat.completions.create(model=self.openai_config.model_name, messages=message).choices[0].message.content
        return response

    def retrieve_data(self, query_embedding):
        # Retrieve relevant data based on the query embedding (dummy example, replace with real retrieval logic)
        return self.elasticsearch_database.search(query_embedding)
