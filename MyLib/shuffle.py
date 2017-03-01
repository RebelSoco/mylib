import random
import os

def shuffle(item):
    x,y = [],[]
    if any(isinstance(x,(int,float,complex)) for x in item) == True:
        raise Exception ('Can only contain type "string"')
    for i in item:
        for L in i:                              
            x += str(L)
        random.seed = (os.urandom(1024))
        random.shuffle(x)
    y += x
    random.seed = (os.urandom(1024))
    random.shuffle(y)
    return ''.join(y)