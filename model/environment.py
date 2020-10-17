import os


class Environment:
    AWS_REGION = os.getenv("REGION")
    TABLE = os.getenv("TABLE")
    QUEUE_NAME = os.getenv("QUEUE_NAME")
