from celery import Celery

app = Celery('tasks', backend='amqp', broker='amqp://')

@app.task
def fib(n):
  a, b = 1, 1;

  for x in range(n-1):
    a, b = b, a + b;
    return x;

print(fib(11));
