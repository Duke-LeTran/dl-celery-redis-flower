# Installation
```
pipenv shell
pipenv install -r requirements.txt
```

# Start the web app
* Start the flask app: `python run.py`
* Start the Celery app: `celery -A run:celery_app worker --loglevel=INF`
