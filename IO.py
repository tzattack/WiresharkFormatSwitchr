import random
import sys
import os
import glob

'''
print(os.path.basename("/a/b/c.txt"))

# Write file
test_file = open("test.txt","wb")
print(test_file.mode)
print(test_file.name)
test_file.write(bytes("Write me to the file\n", 'UTF-8'))
test_file.close()

# Read file

test_file = open("test.txt", "r+")
text_in_file = test_file.read()
print(text_in_file)



# File list with txt files
file_list = glob.glob("./*.txt")
print("TXT file list: ")
print(file_list)


print("File and directory list: ")
print(os.listdir("./"))


i = 0
for file_name in file_list:
    file_name = os.path.basename(file_list[i])
    test_file = open(file_name, "r+")
    text_in_file = test_file.read()
    print(text_in_file)
    i += 1
'''

# a = open("output.txt", "w")
all_file_list = []
for path, subdirs, files in os.walk(r'./'):
    for filename in files:
        f = os.path.join(path, filename)
        # a.write(str(f) + os.linesep)
        all_file_list.append(str(f))

print(all_file_list)

j = 0
txt_file_list = []
for txt_file in all_file_list:
    if all_file_list[j].find(".txt") is not -1:
        print("true!")
        print(all_file_list[j])
        txt_file = all_file_list[j]
        txt_file_list.append(all_file_list[j])
    j += 1

print(txt_file_list)
