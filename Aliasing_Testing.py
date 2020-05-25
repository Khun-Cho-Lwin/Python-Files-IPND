p = ["J", "a", "n", "e", "s"]
q = p
print q
p = [0,0,7]
q = p
print p
print q

spy = [0,0,7]
agent = spy
spy[2] = agent[2] + 1
print spy
