from celery_app import app
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@app.task
def add(x, y, debug=False):
    logger.info('Adding {0} + {1} in {2} mode'.format(x, y, debug))
    return x + y


@app.task
def multiply(x, y):
    logger.info('Multiplying {0} x {1}'.format(x, y))
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
