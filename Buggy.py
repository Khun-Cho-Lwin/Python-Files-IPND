def printExample(a,b):
    print a + b

def printInches(n):
    print str(n) + " inches" #(str)
printExample("long ", "word")
printExample("17   ", "23")
printExample(17, 23)
printInches(42)

def bracket(text):
    return "[" + text + "]"
print bracket("This is an imorotant message.")
def boldwrap(text):
    return "<b>" + text + "<b>"
print boldwrap("This is an imorotant message.")

def remove(somestring, sub):
    """Return somestring with sub removed."""
    location = somestring.find(sub)
    if location == -1:
        return somestring
    length = len(sub)
    part_before = somestring[:location]
    part_after = somestring[location + length:]
    return part_before + part_after

print remove("audacity", "a")
print remove("pythonic", "ic")
print remove("substring institution", "string in")
print remove("ding", "do")
print remove("doomy", "dooming")
