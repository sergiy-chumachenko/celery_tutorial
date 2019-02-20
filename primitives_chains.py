from celery import chain
from tasks.tasks import add, multiply


my_chain = chain(add.s(4, 6) | multiply.s(10))().get()
print(my_chain)  # 100

my_chain_2 = chain(add.s(20, 15) | add.s(10), multiply.s(20))().get()
print(my_chain_2)


# Partial chain
partial_chain = chain(add.s(10) | add.s(20) | multiply.s(12))
print(partial_chain)  # tasks.tasks.add(10) | add(20) | multiply(12)
print(partial_chain(10).get())  # 480

# Simple syntax
print((add.s(10, 4) | add.s(10) | multiply.s(10))().get())  # 240