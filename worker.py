#!/usr/bin/env python
import celeryconfig
from celery import Celery

app = Celery()
app.config_from_object(celeryconfig)

@app.task(name="ping", bind=True)
def do_something(self):
    return("Pong!")

@app.task(name="add")
def add(x, y):
    return x + y