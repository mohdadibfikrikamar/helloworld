##String manipulation functions

name = "Adib"
age = 41

message_1 = f"Hello, my name is {name} and I am {age} years old."

print(message_1)

## Exercise 1

message = """HariNi"""
message_1 = """  HariNi"""

print(len(message))
print(len(message_1))
print(message_1.strip())
print(message.upper())
print(message.lower())
print(message.title())
print(message.replace("i", "e"))

## Exercise 2
## Build  a  simple  text  analyzer  that  counts  words,  characters,  andsentences in a given text.text

message = f"""Python is a powerful programming language. It's easy to learn and versatile!You  can  use  Python  for  web  development,  data  science,  andautomation. The syntax is clean and readable.This makes Python perfect for beginners and experts alike."""

message_1 = f"""Python is a powerful programming language. It's easy to learn \n""""""coding"""

message_2 = f"""My age: {age}"""

print("Number of words:", len(message.split())) ## count words
print("Number of characters:", len(message)) ## characters (ie: alphabets, spaces, numbers)
print("Number of sentences:", message.count(".") + message.count("!") + message.count("?")) 
print("Number of sentences:", message.count("?")) ## count only sentence with question mark
print(message_1)
print("Number of sentences:", message_1.count("a"))
print(message_2)
print(message_2[0:7])
print(message[1])
print(message[-1])