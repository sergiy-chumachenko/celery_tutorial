from tasks.tasks import add


# result = tasks.add.delay(10, 20)
result = add.apply_async(args=[10, 20])
print(result.status)
print(result.result)
print(result.status)
print(result.get())
s1 = add.signature((2, 2), countdown=5)  # 10 sec, countdown
print(s1)
s1 = s1.delay()
print(s1.status)
print(s1.get())
s2 = add.s(10)
print(s2)
s2 = s2.delay(10)
print(s2.get())
s3 = add.s(2, 2, debug=True)
s3 = s3.delay(debug=False)   # debug is now False.
