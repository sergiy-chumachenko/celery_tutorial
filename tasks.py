from celery import Celery
import os

with open('env_script.env') as f:
    for line in f:
        if 'export' not in line:
            continue
        if line.startswith('#'):
            continue
        key, value = line.replace('export ', '', 1).strip().split('=', 1)
        os.environ[key] = value

app = Celery('tasks',
             backend='rpc://',
             broker='amqp://'+ os.environ['BROKER_USER'] +
                    ':' + os.environ['BROKER_PASSWORD'] + '@localhost:5672/' + os.environ['BROKER_VHOST']
             )


@app.task
def add(x, y):
    return x + y
