#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    config.py
# @Author:      Kuro
# @Time:        7/30/2024 11:24 PM

class ElasticConfig:
    index_config = {
        "mappings": {
            "properties": {
                "text": {"type": "text"},
                "embedding": {"type": "dense_vector", "dims": 384}
            }
        }
    }
    index_name = "documents"
    max_len = 50
    host = "localhost"
    port = 9200
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
