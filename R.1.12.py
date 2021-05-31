  
from random import randrange

def my_choice(data):
    a = randrange(0,len(data))
    return data[a]


print(my_choice([2,3,4,5]))