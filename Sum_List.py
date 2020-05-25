def sum_list(list):
    return sum(list)
print sum_list([1,2,3])

def sum_list(list):
    result = 0
    for e in list:
        result = result + e
    return result
print sum_list([1,2,3])
print sum_list([4,5,6])

def sum_list(list):
    result = 2
    for a in list:
        result = result + a
    return result
print sum_list([3,4])

#result variable can change the result because "result = result * a
#if there will be 0,it can't run.
def multiple_list(list):
    result = 2
    for a in list:
        result = result * a
    return result
print multiple_list([3,4])

# Why? Why? Why? --- I don't know.
def division(list):
    result = 0
    for b in list:
        result = result / b
    return result
print division([6,2])
