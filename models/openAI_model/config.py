#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    config.py
# @Author:      Kuro
# @Time:        7/30/2024 11:43 PM
import os

from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), "../../.env")
load_dotenv(dotenv_path)


class OpenAIConfig:
    model_name = "gpt-4o-mini"
    openai_api_key = os.getenv("OPEN_API_KEY")
