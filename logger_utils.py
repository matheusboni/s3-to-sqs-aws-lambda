import logging
import os
import sys


LOG_LEVEL = os.getenv('LOG_LEVEL')

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logger = logging.getLogger('sqs-to-dynamodb-aws-lambda')
logger.setLevel(logging.INFO)

stream_info = logging.StreamHandler(stream=sys.stdout)
stream_info.setLevel(LOG_LEVEL)
stream_info.setFormatter(formatter)

logger.addHandler(stream_info)
