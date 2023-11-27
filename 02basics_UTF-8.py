# COMPLIANCE WITH UTF-8

"""
What is character encoding?

Encoding is way of translating characters (i.e. letters, punctuation marks,
symbols, white spaces, control signs) to numbers and ultimately to bits.
Every character can be encoded to a specific byte sequence.

For every character there's a number value assigned. Here are character groups:
- lowercase letters from the latin alphabet: a-z,
- uppercase letters from the latin alphabet: A-Z,
- punctuation marks and symbols: i.e. $, !,
- whitespace characters: space " ", new line " ", carriage return "\r",
  tabulator "\t" etc.
- Non-writable characters: backspace "\b"; characters that cannot be displayed
  in way like i.e. some number or A letter.

ASCII
-----------

128 characters
Contains 7 bits
Released in 1963
Cannot store specific letters from Polish, Chinese or similar languages

UNICODE
------------

1_114_112 possible codes

The best way to understand it is to imagine some type of a map or a double
column database. In this area Unicode maps characters (for example "a",
":", "3") to specific unique positive numbers.

UTF-8
------------
Implementation of UNICODE

8-bit UNICODE Transformation Format

- uses between 1 to 4 bits to code one character
- it is ASCII compatible
- currently over million characters are coded
- character code has the "U+" prefix
"""

# good use example
text_en = "Hello, young programmers!"
text_fr = "Voiÿ ambiguë d'un cœur qui, au zéphĀr, préfère les jattes de kiwis."
text_cn = "你好,世界"
print(text_en)
print(text_fr)
print(text_cn)

# not good example but it will work
整数 = 7
turtle = "turtle"
vérité = True
print(整数)
print(turtle)
print(vérité)

# -------------------------------
# Coding and Decoding in Python
# -------------------------------
print("résumé".encode("utf-8"))
print(b'r\xc3\xa9sum\xc3\xa9'.decode("utf-8"))

print(ascii('jalepeño'))

print(bin(0)) # returns binary representation of int

print(bytes("🐍", "utf-8"))

# chr
print(chr(97))
print(chr(7048))

# ord - reverse of chr
print(ord("a")) # 97
print(ord("ę")) # 281