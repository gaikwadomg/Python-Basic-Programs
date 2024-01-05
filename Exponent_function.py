print(4 ** 6)

def power_function(base_num , pow_num):
    res = 1
    for x in range(pow_num):
        res = res * base_num
    return res


print(power_function(4,6))
