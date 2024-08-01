#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    config.py
# @Author:      Kuro
# @Time:        7/30/2024 11:24 PM
import os

from pydantic import BaseModel
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "../../.env")
load_dotenv(dotenv_path)

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
    # hosts = "https://10.142.0.2:9200/"
    hosts = "http://localhost:9200/"
    api_key = os.getenv("ELASTIC_API_KEY")

class QueryRequest(BaseModel):
    question: str
