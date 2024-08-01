#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    chatbot_controller.py
# @Author:      Kuro
# @Time:        7/31/2024 9:29 PM
from embeddings.elastic.database import EmbeddingDatabase
from services.chatbot_service import ChatbotService


class ChatbotController:
    def __init__(self, client):
        self.chatbot_service = ChatbotService(EmbeddingDatabase(client))

    def handle_chat(self, user_query: str):
        response = self.chatbot_service.get_response(user_query)
        return response
