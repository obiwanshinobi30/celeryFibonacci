from celery import Celery

app = Celery('fibonacci', backend='amqp', broker='amqp://')

@app.task
def fib(n):
  a, b = 1, 1;

  for x in range(n-1):
    a, b = b, a + b;
    return a;
  return 222;
