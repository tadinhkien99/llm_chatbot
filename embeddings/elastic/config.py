#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    config.py
# @Author:      Kuro
# @Time:        7/30/2024 11:24 PM
import os

from dotenv import load_dotenv
from pydantic import BaseModel

dotenv_path = os.path.join(os.path.dirname(__file__), "../../.env")
load_dotenv(dotenv_path)


class ElasticConfig:
    index_config = {
        "mappings": {
            "properties": {
                "text": {
                    "type": "text"
                },
                "embedding": {
                    "type": "dense_vector",
                    "dims": 1536
                }
            }
        }

    }
    index_name = "documents"
    # hosts = "http://localhost:9200/"
    # hosts = "https://10.142.0.2:9200/"
    hosts = "http://35.227.17.180:5601/"
    api_key = os.getenv("ELASTIC_API_KEY")


class QueryRequest(BaseModel):
    question: str
