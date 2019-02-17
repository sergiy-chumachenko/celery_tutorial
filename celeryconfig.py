import os

with open('env_script.env') as f:
    for line in f:
        if 'export' not in line:
            continue
        if line.startswith('#'):
            continue
        key, value = line.replace('export ', '', 1).strip().split('=', 1)
        os.environ[key] = value

broker_url = 'amqp://' + os.environ['BROKER_USER'] + ':' + os.environ['BROKER_PASSWORD'] + \
             '@localhost:5672/' + os.environ['BROKER_VHOST']
result_backend = 'redis://:' + os.environ['BACKEND_REDIS_PASSWORD'] + '@' + \
                 os.environ['BACKEND_REDIS_HOST'] + ':' + os.environ['BACKEND_REDIS_PORT'] + '/0'

imports = ('tasks.tasks', 'soup.tasks', )
task_routes = ([
    ('soup.tasks.*', {'queue': 'soup'}),
    ('tasks.tasks.*', {'queue': 'tasks'}),
],)
# task_serializer = 'json'
# result_serializer = 'json'
# accept_content = ['json']
# timezone = 'Europe/Oslo'
# enable_utc = True
