from celery import Celery
import time

app = Celery('tasks', broker='amqp://localhost//',
             backend='db+scheme://user:password@host:port/dbname')


@app.task
def reverse(string):
    time.sleep(10)
    return string[::-1]
