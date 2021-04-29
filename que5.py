# targil 5
# map function
def map_func(func, lst):
    arr = []
    for x in lst:
        arr.append(func(x))
    return arr

def multi(x):
    return x*2

print(map_func(multi, [1, 2, 3]))