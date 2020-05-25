print "test".find("t")
print "test".find("t",1)

first_location = "test".find("t")
print"test".find("t",first_location+1)

example = "Wow! Python is great! Don't you think?"
first = example.find("!")
second = example.find("!", first + 1)
new_string = example[:first] + example[first+1:second] + example[second+1:]
print new_string
new_string = example[:first] + "." + example[first+1:second] + "." + example[second+1:]
print new_string
