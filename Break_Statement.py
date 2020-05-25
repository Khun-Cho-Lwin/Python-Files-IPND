def print_numbers(n):
    i = 1
    while i <= n:
        print i
        i = i + 1
print print_numbers(3)

def print_numbers(n):
    i = 1
    while True:
        if i > n:
            break
        print i
        i = i + 1
print print_numbers(3)
