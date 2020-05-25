i = 0
while i < 10:
    print i
    i = i + 1

i = 0
while i != 10:
    i = i + 1
    print i
#While loop (2)
i = 2 #(*****)
while i != 10:
    i = i + 2
    print i

#While loop playground
i = 0
while i < 10:
    print i
    i = i + 1
#my Test
i = 0
while i < 10:
    i = i + 1
    print i

def remove_spaces(text):
    text_without_spaces = ""
    while text != "":
        next_character = text[0]
        if next_character != " ":
            text_without_spaces = text_without_spaces + next_character
        text = text[1:]
    return text_without_spaces
print remove_spaces("hello my name is andy how are you?")
