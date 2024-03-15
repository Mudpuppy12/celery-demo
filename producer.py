#!/usr/bin/env python

import logging
import celeryconfig

from celery import Celery

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app=Celery()
app.config_from_object(celeryconfig)

async_result = app.send_task(name="ping")
logger.info(async_result)

async_result = app.send_task(name="add",args=[5,2])
logger.info(async_result)


