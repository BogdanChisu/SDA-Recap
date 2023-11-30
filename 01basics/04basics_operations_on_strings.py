"""
---------------------
Operations on Strings
---------------------
"""
print(f"The firs letter of the sentence 'Alice has a cat.' is "
      f"{'Alice has a cat.'[0]}")
hello = 'Hello, World'
print(hello[7])

"""
---------------------
The len() function
---------------------
"""
sentence = "Lorem ipsum dolor sit amet..."
print(len(sentence))
print(len("Alice has a cat."))

"""
---------------------
The .index() function
---------------------
"""
hello = "Hello, World!"
print(hello.index('o')) # returns the first location only

"""
---------------------
The .count() function
---------------------
"""
hello = "Hello, World!"
print(hello.count('o')) # returns the number of occurrences

"""
---------------------
String slicing
---------------------
"""
# It gets a substring (substring) from the character chain
hello = "Hello, World!"
print(hello[7:12])# returns World
print(hello[7:12:2])# returns Wrd

test = "Test string"
print(test[:4])
print(test[5:])
print(test[:]) # returns the entire string

# reverse a string
hello = "Hello, World!"
print(hello[::-1])

"""
---------------------
.lower(), .upper(), .title() function
---------------------
"""
hello = "Hello, World!"
print(hello.lower()) # return hello, world!
print(hello.upper())
print(hello.title())

"""
---------------------
.replace() function
---------------------
"""
hello = "Hello, World!"
print(hello.replace('l', 'Z'))