print "test".find("te")
print "test".find("st")
print "test"[2:]

my_string = "test"
print my_string.find("te")
print my_string.find("st")
print my_string[2:]

my_string = "My favorite color: blue"
color_start_location = my_string.find("color:")
favorite_color = my_string[color_start_location:]
print favorite_color
print favorite_color[7:]
