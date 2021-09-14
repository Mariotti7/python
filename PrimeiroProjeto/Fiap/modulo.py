import math
import random
import emojis

num= random.randint(1,100)
raiz=math.sqrt(num)

print(emojis.encode('A raiz de {} é {:.2f} :poop:'.format(num, raiz)))