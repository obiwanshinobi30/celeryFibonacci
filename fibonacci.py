from celery import Celery

app = Celery('fibonacci', backend='amqp', broker='amqp://')

@app.task
def fib(n):
  a, b = 0, 1;

  for x in range(n):
    a, b = b, a + b;
  return a;
