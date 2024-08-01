#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    database.py
# @Author:      Kuro
# @Time:        7/30/2024 11:25 PM

from elasticsearch import Elasticsearch, helpers
from langchain_text_splitters import RecursiveCharacterTextSplitter

from embeddings.elastic.config import ElasticConfig


class EmbeddingDatabase:
    def __init__(self, client):
        """
        Initialize the OpenAIEmbedding with a SentenceTransformer model and Elasticsearch self.client.
        """
        self.config = ElasticConfig()
        self.index_name = self.config.index_name
        self.client = client      

    def create_index(self):
        """
        Create the Elasticsearch index with the appropriate mapping for dense vectors.
        """
        if not self.client.indices.exists(index=self.index_name):
            self.client.indices.create(index=self.index_name, body=self.config.index_config)

    def split_into_chunks(self, text):
        """
        Split text into chunks of a specified maximum length.
        """
        text_splitter = RecursiveCharacterTextSplitter.from_tiktoken_encoder(chunk_size=512, chunk_overlap=256)
        chunks = text_splitter.split_text(text)
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

        helpers.bulk(self.client, actions)

    def search(self, embedding, n_results=5):
        """
        Search for similar documents given a query.
        """

        script_query = {
            "script_score": {
                "query": {"match_all": {}},
                "script": {
                    "source": "cosineSimilarity(params.query_vector, 'embedding') + 1.0",
                    "params": {"query_vector": embedding}
                }
            }
        }

        response = self.client.search(
            index=self.index_name,
            body={
                "size": n_results,
                "query": script_query,
                "_source": {"includes": ["text"]}
            }
        )

        return response['hits']['hits']
