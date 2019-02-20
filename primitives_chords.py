from celery import chord, group
from tasks.tasks import add, multiply, xsum

# A chord is a group with a callback:
my_chord = chord((add.s(10, i) for i in range(5)), xsum.s())()
print(my_chord)  # c1327e82-7538-4096-a382-c49d0ee66130
print(type(my_chord))  # <class 'celery.result.AsyncResult'>
print(my_chord.get())  # 60

# A group chained to another task will be automatically converted to a chord:
print((group(add.s(10, i) for i in range(3)) | xsum.s())().get())  # 33

