def my_func(x,y,z):
    if x > z and y > z:
        return x + y
    elif y > x and z > x:
        return y + z
    else:
        return z + x

print(my_func(1,1,1))



