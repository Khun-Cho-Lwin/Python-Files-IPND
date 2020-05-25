p = [1,2]
p.append(3)
print "p = "+ str(p)
p = p + [4,5]
print "p = "+ str(p)
print "len(p) = "+ str (len(p))

a = [1,2]
b = [3,4]
a.append(b) #**
#a = a + b  #**
print "b = "+ str(b)
print "a = "+ str(a)
print "len(a) = "+ str(len(a))

p = [7,8]
p = p + [5,6]
print p

p = [5,0]
p.append(7)
print p
