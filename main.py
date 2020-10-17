import json
from datetime import datetime

from repository.payment_repository import PaymentRepository

payment_repository = PaymentRepository()


def handler(event, _):
    try:
        for record in event['Records']:
            payment = json.loads(record['body'])

            if payment.get('status') == 'PROCESSED' and payment.get('purchase_id') is not None:
                payment['date'] = datetime.now().isoformat()[:-3]
                payment_repository.save(payment)
                print("Payment: {} was saved".format(payment))
            else:
                print("Payment: {} was not processed successfully".format(payment))

    except Exception as e:
        print('Exception occurred: {}'.format(e))
        raise e

    response = dict(
        status=200,
        message='Event processed successfully'
    )

    return json.dumps(response)
