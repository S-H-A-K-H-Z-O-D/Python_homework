# ' - single quote
# " - double quote
# \ - back slash
# / - forward slash
# \n - newline character
# \' - single quote
# \" - double quote
# \t - tab
# \\ - backslash

hello = "Hello \nW\norld"


word = 'I\'m a teacher'
# print(word)
# print(hello)


directorry = r"D:\Python\bi-and-ai-talents\lesson-2\homework"
# print(type(directorry))
# print(directorry)

#         0123456789
my_str = "Hello World" # Sequence
# print(len(my_str))

# Slicing or Indexing
# BEGIN:END:STEP
# print(my_str[:4] + my_str[5:])
# print(my_str[::2])

#       -10
my_str = "Hello World" # Sequence

# print(my_str[-5:])

# SyntaxError
# TypeError
# ValueError
# IndexError: string index out of range

# Mutable vs Immutable (O'zgaruvchan vs O'zgarmas)

my_str = "Apple"
print("Oldin:", id(my_str))

my_str2 = 'a' + my_str[1:]
print("Keyin:", id(my_str))

print(my_str, my_str2)

# object.method()


