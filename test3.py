import random




allnum = random.sample(range(75), 25)

r = [[allnum.pop() for x in range(5)] for _ in range(5)]

print(r)
