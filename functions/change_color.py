from random import randint #choice
 
def change_color():
    r = randint(0, 255)
    b = randint(0, 255)
    g = randint(0, 255)
    #return ["#"+''.join([choice('ABCDEF0123456789') for i in range(6)])]
    return (r,g,b)
        