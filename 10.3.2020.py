p = [0,1,2]
print p.index(1)
p = [0,1,3,2,2]
print p.index(2)

spy = [1,2,3]
def replace_spy(sp):
    spy[2] += 1
    return sp
print replace_spy

def find_element(a,b):
    i = 0
    for item in a:
        if item == b:
            return i
        i += 1
    else:
        return -1
print find_element([1,2,3],3)

print (type(1/2))

x = 4.5
y = 2
print x//y

x = True
y = False
z = False
if x or y and z:
    print ("yes")
else:
    print ("no")

x = True
y = False
z = False

if not x or y:
    print(1)
elif not x or not y and z:
    print(2)
elif not x or y or not y and x:
    print(3)
else:
    print(4)

counter = 1
def doLotsOfStuff():
    global counter
    for i in (1,2,3):
        counter += 1
doLotsOfStuff()
print counter

print r"\nwoow"
print "\x48\x49!"
print(0xA + 0xa)

print (2 ^ 31) -1

def sum_list(list):
    result = 0
    for e in list:
        result = result + e
    return result
print sum_list([3,6])

height = input("Enter Height of Rectangle:")
width = input("Enter width of Rectangle:")
area = int(height) * int(width)
print("Area is ",area)
