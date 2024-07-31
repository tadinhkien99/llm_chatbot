#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    document_service.py
# @Author:      Kuro
# @Time:        7/31/2024 11:20 PM
import os

from embeddings.elastic.create_embedding import EmbeddingIndexer
from embeddings.elastic.database import EmbeddingDatabase


class DocumentService:
    def __init__(self, data_path):
        """
        Initialize the DocumentService with an EmbeddingDatabase instance.
        """
        self.db = EmbeddingDatabase()
        self.embeddings = EmbeddingIndexer()

    def load_data(self, data_path):
        for file in os.listdir(data_path):
            with open(os.path.join(data_path, file), "r") as f:
                text = f.read()
                self.index_document(text)
    def index_document(self, text):
        """
        Index a document into Elasticsearch.
        """
        chunks = self.db.split_into_chunks(text)
        embeddings = self.embeddings.create_embedding(chunks)
        self.db.index_chunks(chunks, embeddings)

