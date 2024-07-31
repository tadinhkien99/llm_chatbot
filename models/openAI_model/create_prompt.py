#!/usr/bin/env python
# -*- coding:utf-8 -*-
# @Filename:    create_prompt.py
# @Author:      Kuro
# @Time:        7/30/2024 11:43 PM

class CreatePrompt:
    def __init__(self, role, content):
        self.role = role
        self.content = content

    def create_prompt(self):
        return {"role": self.role, "content": self.content}

