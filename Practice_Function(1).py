def say_hello():
    return "Hello!"
print say_hello()

def say_hello(name):
    greeting = "Hello " + name + " !"
    return greeting
print say_hello("Miriam")
print say_hello("Andy")
