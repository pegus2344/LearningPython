import random

for i in range (10):
   x=random.random()
   print x
for i in range (5):
   y=random.randint(5, 25)
   print 'randint: ' + str(y)

for i in range(3):
   t=[1,2,3,4,5,6,7,8,9,10]
   z=random.choice(t)
   print 'choice is ' +str(z)


