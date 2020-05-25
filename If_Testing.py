def absolute (x):
    if x < 0:
        x = -x
        return x
print absolute(-5)
# print absolute(6)

def absolute(x):
    if x < 0:
        x = -x
        return x
    else:
        return x
print absolute(6)
print absolute(-5)
