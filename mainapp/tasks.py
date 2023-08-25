from celery import shared_task


@shared_task
def test_func():
    return 'Task Done'


@shared_task
def print_hello():
    return "Hello Siva !"
