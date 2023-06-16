from celery import shared_task

@shared_task(ignore_result=False)
def add(x, y):
    return x + y

@shared_task(ignore_result=False)
def multiply(x, y):
    return x * y
