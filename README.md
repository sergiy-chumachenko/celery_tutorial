# Celery Tutorial 
### Installation (Ubuntu 18.04)
#### Update 
```
$ sudo apt update && apt upgrade
```
#### Virtual Environment Configuration
```
$ mkdir my_project
$ cd my_project
$ virtualenv .env
$ source /.env/bin/activate
```
#### Install Celery
```
$ pip install celery
```
#### RabbitMQ Installation
Setting up RabbitMQ
To use Celery we need to create a RabbitMQ user, a virtual host and allow that user access to that virtual host:
```
$ sudo apt install rabbitmq-server
$ sudo rabbitmqctl add_user myuser mypassword
$ sudo rabbitmqctl add_vhost myvhost
$ sudo rabbitmqctl set_user_tags myuser mytag
$ sudo rabbitmqctl set_permissions -p myvhost myuser ".*" ".*" ".*"
```
#### Starting/Stopping the RabbitMQ server
To start the server:
```
$ sudo rabbitmq-server
```
you can also run it in the background by adding the -detached option (note: only one dash):
```
$ sudo rabbitmq-server -detached
```
Never use kill (kill(1)) to stop the RabbitMQ server, but rather use the rabbitmqctl command:
```
$ sudo rabbitmqctl stop
```

#### RabbitMQ Configuration and Management
```
sudo rabbitmqctl status
sudo rabbitmqctl stop
sudo rabbitmq-server start
broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost'
```

#### Celery App Configuration (tasks.py)
```
app = Celery('tasks',
             backend='rpc://',
             broker='amqp://myuser:mypassword@localhost:5672/myvhost')
```

#### Install Flower - Celery monitoring tool
##### https://flower.readthedocs.io/en/latest/index.html
```
$ pip install flower
```
##### RabbitMQ Management Api Configuration
```
$ sudo rabbitmqctl set_user_tags myuser administrator
$ sudo rabbitmq-plugins enable rabbitmq_management
$ sudo service rabbitmq-server restart
```
#### Redis for Result Backend
##### Install Redis
In Terminal:

`$ sudo apt install redis-server`

In Virtual Environment:

`pip install redis`

##### Configuring a Redis Password
`$ sudo nano /etc/redis/redis.conf`

Scroll to the SECURITY section and look for a commented directive that reads:

`# requirepass foobared`

Uncomment it by removing the #, and change foobared to a secure password.

`$ sudo systemctl restart redis.service`

#### Create env script env_script.env in project directory
```
export BROKER_USER={RabbitMQ USER}
export BROKER_PASSWORD={RabbitMQ PASSWORD}
export BROKER_VHOST={RabbitMQ VHOST}
export BACKEND_REDIS_PASSWORD={Redis PASSWORD}
export BACKEND_REDIS_HOST={Redis HOST} #default 127.0.0.1
export BACKEND_REDIS_PORT={Redis PORT} #default 6379
```
#### Modify Celery Configuration (tasks.py)
```
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
             backend='redis://:' + os.environ['BACKEND_REDIS_PASSWORD'] + '@' +
                     os.environ['BACKEND_REDIS_HOST'] + ':' + os.environ['BACKEND_REDIS_PORT'] + '/0',
             broker='amqp://' + os.environ['BROKER_USER'] +
                    ':' + os.environ['BROKER_PASSWORD'] + '@localhost:5672/' + os.environ['BROKER_VHOST']
             )
```

#### Running the Celery worker server
You can now run the worker by executing our program with the worker argument:
```
$ celery -A app worker -l info
```
#### Running the Flower server
```
$ celery -A tasks flower --broker_api=http://user:password@localhost:15672/api/vhost
```
