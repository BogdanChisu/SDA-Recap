"""
----------------
FILE OPEN MODES
----------------

Files can be opened in several modes, depending on what the use is. The
second parameter of the open() function is called mode.

r - read access (default option)
w - write, if the file doesn't exist, it is created, also if an older file
    exists, it gets overwritten
x - execute, it will fail if a file already exists
a - add, if the file doesn't exist it will be created
b - binary mode
t - text mode (default option)
+ - this means that a cursor will be set at the end of the file. By default
    it is placed at the start of the file

---------------------
File Opening Method 1
---------------------
"""

# f = open('file.txt')
#
# # ...
#
# f.close()

# NOT RECOMMENDED - IF THERE IS AN ERROR, THE FILE WILL NOT CLOSE

"""
---------------------
File Opening Method 2
---------------------
"""

# with open('file.txt') as file_variable:
#     #
#
# print("OK")

# THIS WAY, THE FILE IS CLOSED AUTOMATICALLY

"""
Reading a file
"""

# with open('other/file.txt') as f:
#     lines = f.readlines()
#
#     for line in lines:
#         print(line)

# with open('other/file.txt') as f:
#
#     for line in f:
#         print(line, end='')

# -------------------------
# Read a file byte by byte
# -------------------------

# with open('other/file.txt') as f:
#     content = f.read(4)
#     f.tell() # write 4
#     content = f.read(4)
#     f.tell() # write 8
#     f.seek(0) # the cursor gets ack to the file's starting point

"""
-------------
Saving a file
-------------
"""

with open('other/sample.txt', 'w') as f:
    for i in range(10):
        f.write(f'This is line number: {i}\n')