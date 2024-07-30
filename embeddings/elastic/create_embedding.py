#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    create_embedding.py
# @Author:      Kuro
# @Time:        7/30/2024 11:24 PM

from sentence_transformers import SentenceTransformer


class EmbeddingIndexer:
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        """
        Initialize the EmbeddingIndexer with a SentenceTransformer model and Elasticsearch client.
        """
        self.model = SentenceTransformer(model_name)

    def create_embedding(self, sentences):
        """
        Create embeddings for a list of sentences.
        """
        return self.model.encode(sentences, convert_to_numpy=True)
