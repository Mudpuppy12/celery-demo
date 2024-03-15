Example Celery SQS queue with DynamoDB backend

0. Make sure your aws credentials are good (Run the s3_test.py)
1. Create a standard SQS Queue named celery in AWS 
2. Create A DynamoDB table called celery_results with a Partion Key ('id') set as a string format.
3. Start a worker celery -A worker worker --loglevel=INFO
4. Run producer, note ID's.
5. Use async_result to see results.

