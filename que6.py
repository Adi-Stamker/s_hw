# question 6
# decorator cache
decorator_cache = dict()

def mul(a,b):
    combined_args = str(a) + str(b)
    if combined_args in decorator_cache.keys():
        return decorator_cache.get(combined_args)
    mul_result = a*b
    decorator_cache.update({combined_args : mul_result})
    return mul_result

print("mul result:", mul(6,7))
print("mul result:", mul(3,2))
print("mul result:", mul(6,7))