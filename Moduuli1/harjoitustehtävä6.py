import random
#Generate 5 random numbers between 10 and 30
randomlist = random.sample(range(0, 9), 3)
for i in randomlist:
    print(i,end=' ')

print('\n')
randomlist = random.sample(range(1, 6), 4)
for i in randomlist:
    print(i,end=' ')