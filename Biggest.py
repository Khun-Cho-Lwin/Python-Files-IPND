def biggest(a,b,c):
    return max(a,b,c)
print biggest(5,6,7)
print biggest(1,3,9)



def biggest(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
print biggest(2,8,9)
print biggest(6,7,5)



def bigger(a,b):
    if a > b:
        return a
    else:
        return b
def biggest(a,b,c):
    return bigger(bigger(a,b), c)
print biggest(3,4,8)
