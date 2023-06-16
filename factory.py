from celery import Celery, Task
from flask import Flask
from config import CELERY_BROKER_URL, CELERY_RESULT_BACKEND

def celery_init_app(app: Flask) -> Celery:
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app

def create_app() -> Flask:
    """
    Celery configurations: https://docs.celeryq.dev/en/stable/userguide/configuration.html
    """
    app = Flask(__name__, template_folder='app/templates')
    app.config.from_mapping(
        CELERY=dict(
            broker_url=CELERY_BROKER_URL,
            result_backend=CELERY_RESULT_BACKEND,
            task_ignore_result=True,
            broker_connection_retry_on_startup=True
        ),
    )
    app.config.from_prefixed_env()
    celery_init_app(app)
    return app