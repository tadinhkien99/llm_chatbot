#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    database.py
# @Author:      Kuro
# @Time:        7/30/2024 11:25 PM

from elasticsearch import Elasticsearch, helpers


class EmbeddingDatabase:
    def __init__(self, model, config, es_host='localhost', es_port=9200, index_name='documents'):
        """
        Initialize the EmbeddingIndexer with a SentenceTransformer model and Elasticsearch client.
        """
        self.model = model
        self.es = Elasticsearch([{'host': es_host, 'port': es_port}])
        self.index_name = index_name
        self.config = config

    def create_index(self):
        """
        Create the Elasticsearch index with the appropriate mapping for dense vectors.
        """
        if not self.es.indices.exists(index=self.index_name):
            self.es.indices.create(index=self.index_name, body=self.config.index_config)

    def split_into_chunks(self, text):
        """
        Split text into chunks of a specified maximum length.
        """
        max_len = self.config.max_len
        words = text.split()
        chunks = [' '.join(words[i:i + max_len]) for i in range(0, len(words), max_len)]
        return chunks

    def index_chunks(self, chunks, embeddings):
        """
        Index the given chunks and their embeddings into Elasticsearch.
        """
        actions = [
            {
                "_index": self.index_name,
                "_source": {
                    "text": chunk,
                    "embedding": embedding.tolist()
                }
            }
            for chunk, embedding in zip(chunks, embeddings)
        ]

        helpers.bulk(self.es, actions)
