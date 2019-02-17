from celery import group
from tasks.tasks import add, multiply

res = group(add.s(i, i) for i in range(10))()
print(res.get())

lazy_group = group([add.s(10, 10), add.s(20, 20)])()
print(lazy_group.get())

g = group(add.s(i) for i in range(10))
print(g)
print(g(10).get())
