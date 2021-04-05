import json
from datetime import datetime

from logger_utils import logger
from repository.payment_repository import PaymentRepository

payment_repository = PaymentRepository()


def handler(event, _):
    try:
        for record in event['Records']:
            payment = json.loads(record['body'])

            if payment.get('status') == 'PROCESSED' and payment.get('purchaseId') is not None:
                payment['date'] = datetime.now().isoformat()[:-3]
                payment_repository.save(payment)
                logger.info("Payment: {} was saved".format(payment))
            else:
                logger.warn("Payment: {} was not processed successfully".format(payment))

    except Exception as e:
        logger.exception('Exception occurred: ', e)
        raise e

    response = dict(
        status=200,
        message='Event processed successfully'
    )

    return json.dumps(response)
