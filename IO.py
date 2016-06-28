import random
import sys
import os
import glob
import subprocess

from builtins import print

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
for path, subdirectories, files in os.walk(r'.'):
    for filename in files:
        f = os.path.join(path, filename)
        # a.write(str(f) + os.linesep)
        all_file_list.append(str(f))
print("All the files in directory and subdirectory: ")
print(all_file_list)

'''
Text file capturing
'''

j = 0
txt_file_list = []
for txt_file_item in all_file_list:
    if all_file_list[j].find(".txt") is not -1:
        txt_file = all_file_list[j]
        txt_file_list.append(txt_file)
    j += 1
print("All the txt file: ")
print(txt_file_list)

k = 0
for text in txt_file_list:
    # Get file name
    txt_file_name = os.path.basename(txt_file_list[k])

    # Get absolute directory from relative directory
    script_dir = os.path.dirname(__file__)
    rel_path = txt_file_list[k]
    abs_file_path = os.path.join(script_dir, rel_path)

    # Open files
    text_file = open(abs_file_path, "r+")
    text_in_file = text_file.read()

    print("TEXT IN " + txt_file_name + ": ")
    print(text_in_file)

    # Write into new files
    script_output_dir = os.path.dirname(__file__)
    rel_output_path = "./output/"
    abs_output_file_path = os.path.join(script_output_dir, rel_output_path)
    text_output_file = open(abs_output_file_path + txt_file_name, "wb")
    text_output_file.write(bytes(text_in_file, 'UTF-8'))
    text_output_file.close()
    print("Wrote into " + txt_file_name + " succeeded! \n\n")

    k += 1

'''
pcapng file converting
'''
pcapng = 0
pcapng_file_list = []
for pcapng_file in all_file_list:
    if all_file_list[pcapng].find(".pcapng") is not -1:
        pcapng_file = all_file_list[pcapng]
        pcapng_file_list.append(pcapng_file)
    pcapng += 1
print("All the pcapng file: ")
print(pcapng_file_list)

pcapng = 0
for content in pcapng_file_list:
    # Get file name
    file_name = os.path.basename(pcapng_file_list[pcapng])
    print(file_name)
    subprocess.call(["echo", "Hello, world!"], shell=True)
    subprocess.call(["editcap", "-F", "cap", file_name, "output.cap"], shell=True)
    '''
    # Get absolute directory from relative directory
    script_dir = os.path.dirname(__file__)
    rel_path = pcapng_file_list[pcapng]
    abs_file_path = os.path.join(script_dir, rel_path)

    # Open files
    text_file = open(abs_file_path, "r+")
    text_in_file = text_file.read()

    print("*******Content IN " + file_name + ": ")
    print(text_in_file)


    # Write into new files
    script_output_dir = os.path.dirname(__file__)
    rel_output_path = "./output/"
    abs_output_file_path = os.path.join(script_output_dir, rel_output_path)
    text_output_file = open(abs_output_file_path + txt_file_name, "wb")
    text_output_file.write(bytes(text_in_file, 'UTF-8'))
    text_output_file.close()
    print("Wrote into " + txt_file_name + " succeeded! \n\n")
    '''
    pcapng += 1
