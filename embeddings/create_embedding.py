#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    create_embedding.py
# @Author:      Kuro
# @Time:        7/30/2024 11:24 PM
from openai import OpenAI

from models.openAI_model.config import OpenAIConfig


class OpenAIEmbedding:
    def __init__(self, client):
        """
        Initialize the OpenAIEmbedding with a SentenceTransformer model and Elasticsearch client.
        """
        self.client = client
        self.batch_size = 32

    def create_embedding_documents(self, sentences):
        """
        Create embeddings for a list of sentences.
        """
        embeddings = []
        for i in range(0, len(sentences), self.batch_size):
            batch_sentences = sentences[i:i + self.batch_size]
            batch_embedding = self.client.embeddings.create(input=batch_sentences, model="text-embedding-3-small").data
            batch_embedding = [embedding.embedding for embedding in batch_embedding]
            embeddings.extend(batch_embedding)
        return embeddings

    def create_embedding(self, sentence):
        """
        Create an embedding for a single sentence.
        """
        embedding = self.client.embeddings.create(input=sentence, model="text-embedding-3-small").data[0].embedding
        return embedding
