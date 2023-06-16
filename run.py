from app import celery_app, flask_app


if __name__ == '__main__':
    #from app import views#, models
    flask_app.run(debug=True)