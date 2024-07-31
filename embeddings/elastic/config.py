#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    config.py
# @Author:      Kuro
# @Time:        7/30/2024 11:24 PM
from pydantic import BaseModel


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

class QueryRequest(BaseModel):
    question: str
