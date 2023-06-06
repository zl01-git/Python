def generator():
    for i in range(10):
        yield i

print(next(generator()))
