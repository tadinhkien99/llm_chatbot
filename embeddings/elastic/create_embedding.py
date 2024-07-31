#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    create_embedding.py
# @Author:      Kuro
# @Time:        7/30/2024 11:24 PM
from openai import OpenAI

from models.openAI_model.config import OpenAIConfig


class EmbeddingIndexer:
    def __init__(self):
        """
        Initialize the EmbeddingIndexer with a SentenceTransformer model and Elasticsearch client.
        """
        self.client = OpenAI(api_key=OpenAIConfig.openai_api_key)

    def create_embedding(self, sentences):
        """
        Create embeddings for a list of sentences.
        """
        embeddings = []
        for text in sentences:
            embedding = self.client.embeddings.create(input=[text], model="text-embedding-3-small").data[0].embedding
            embeddings.append(embedding)
        return embeddings
