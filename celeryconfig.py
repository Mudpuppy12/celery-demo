# GENERAL
aws_access_key = ""
aws_secret_key = ""

# BROKER
sqs_queue_url = "https://sqs.us-east-1.amazonaws.com/106613608949/celery"
broker_url=f"sqs://{aws_access_key}:{aws_secret_key}@"
broker_connection_retry_on_startup=True
broker_connection_retry=True
task_create_missing_queues=False

broker_transport_options={
        "region": "us-east-1",
        "predefined_queues": {
            "celery": {
                "url": sqs_queue_url,
                "access_key_id": aws_access_key,
                "secret_access_key": aws_secret_key,
            }
        },
    }

# RESULTS BACKEND
result_backend = 'dynamodb://@us-east-1/celery_results'




