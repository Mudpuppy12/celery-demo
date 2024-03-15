#!/usr/bin/env Python

import celeryconfig

from celery.result import AsyncResult
from celery import Celery

app=Celery()
app.config_from_object(celeryconfig)


res = AsyncResult('2740ffe9-ee24-47d7-a221-38f2aa8c59b7',app=app)

print(res.state)
print(res.get()) 