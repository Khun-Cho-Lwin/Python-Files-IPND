def find_element(xlist,y):
    i = 0 # That's very important to get a result.Its can change the result.
    for item in xlist:
        if item == y:
            return i
        i = i + 1
    else:
        return -1
print find_element([1,2,7],3)
print find_element(['alpha','beta',"gamma"],'gamma')

def find_element(p,t):
    i = 0 # The len of (p) is 3 .So, we can't do inicial no-4.
    while i < len(p):
        if p[i] == t:
            return i
        i = i + 1
    return "Not found !"
print find_element(["alpha","beta","gamma"],"gamma")
print find_element([1,2,7],3)
