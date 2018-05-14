# Celery Tutorial 
### Installation
#### 1. Erlang
```
wget https://packages.erlang-solutions.com/erlang-solutions_1.0_all.deb
sudo dpkg -i erlang-solutions_1.0_all.deb
sudo apt-get update
sudo apt-get install esl-erlang=1:19.3.6
```
#### 2. RabbitMQ
```
For Linux Ubuntu 16.04:
echo "deb https://dl.bintray.com/rabbitmq/debian xenial main" | sudo tee /etc/apt/sources.list.d/bintray.rabbitmq.list
wget -O- https://dl.bintray.com/rabbitmq/Keys/rabbitmq-release-signing-key.asc |
     sudo apt-key add -
sudo apt-get update
sudo apt-get install rabbitmq-server
```
#### 3. Celery
```
pip install celery
```
#### 4. SQLAlchemy & psycopg2
```angular2html
pip install sqlalchemy
pip install psycopg2
pip install psycopg2-binary
```
### RabbitMQ Configuration and Management
```
sudo rabbitmqctl status
sudo rabbitmqctl stop
sudo rabbitmq-server start
broker_url = 'amqp://myuser:mypassword@localhost:5672/myvhost'
```
### Celery Management
```
celery -A tasks worker --loglevel=info
```