# Installation
```
pipenv shell
pipenv install -r requirements.txt
```

# Quick Start
* Start redis: `docker run -p 6379:6379 -d --rm --name redis-duke redis:7-alpine`
* Start the flask app: `python run.py`
* Start the Celery app: `celery -A run:celery_app worker --loglevel=INF`

You may need to check for ip address of the redis docker
```
docker inspect redis-duke
docker network ls
docker inspect network-name
```

# TO-DO
* test celery tasks.py in html pages
* add flower
* add Dockerfile
* add docker-compose.yml
