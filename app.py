# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 19:54:19 2019

@author: Admin
"""

from flask import Flask

app=Flask(__name__)


@app.route("/")
def home():
    return "Hello Flask 2"

@app.route("/test")
def test():
    return "This is Test"

if __name__ == "__main__":
    app.run()
