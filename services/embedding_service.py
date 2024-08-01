#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    embedding_service.py
# @Author:      Kuro
# @Time:        7/31/2024 11:20 PM
import os

from embeddings.create_embedding import OpenAIEmbedding
from embeddings.elastic.config import ElasticConfig
from embeddings.elastic.database import EmbeddingDatabase


class EmbeddingService:
    def __init__(self, client):
        """
        Initialize the EmbeddingService with an EmbeddingDatabase instance.
        """
        self.elasticsearch_config = ElasticConfig()
        self.embeddings = OpenAIEmbedding()

        self.elasticsearch_database = EmbeddingDatabase(client)
        self.elasticsearch_database.create_index()

    def load_data(self, data_path):
        print("Loading data...")
        for file in os.listdir(data_path):
            with open(os.path.join(data_path, file), "r") as f:
                text = f.read()
                self.index_document(text)
        print("Data loaded successfully.")

    def index_document(self, text):
        """
        Index a document into Elasticsearch.
        """
        chunks = self.elasticsearch_database.split_into_chunks(text)
        embeddings = self.embeddings.create_embedding(chunks)
        self.elasticsearch_database.index_chunks(chunks, embeddings)
