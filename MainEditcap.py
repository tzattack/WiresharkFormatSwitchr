import os
import subprocess

'''
Loading all file list
'''
all_file_list = []
for path, subdirectories, files in os.walk(r'.'):
    for filename in files:
        file = os.path.join(path, filename)
        all_file_list.append(str(file))
print("All the files in directory and subdirectory: ")
print(all_file_list)
print("-------------------------------------------------------------")

'''
pcapng file converting
'''
counter = 0
convert_file_list = []
for convert_file in all_file_list:
    if all_file_list[counter].find(".snoop") is not -1:
        convert_file = all_file_list[counter]
        convert_file_list.append(convert_file)
    if all_file_list[counter].find(".pcap") is not -1:
        convert_file = all_file_list[counter]
        convert_file_list.append(convert_file)
    if all_file_list[counter].find(".cap") is not -1:
        convert_file = all_file_list[counter]
        convert_file_list.append(convert_file)
    if all_file_list[counter].find(".libpcap") is not -1:
        convert_file = all_file_list[counter]
        convert_file_list.append(convert_file)
    if all_file_list[counter].find(".5vw") is not -1:
        convert_file = all_file_list[counter]
        convert_file_list.append(convert_file)
    if all_file_list[counter].find(".txt") is not -1:
        convert_file = all_file_list[counter]
        convert_file_list.append(convert_file)
    if all_file_list[counter].find(".ncf") is not -1:
        convert_file = all_file_list[counter]
        convert_file_list.append(convert_file)
    counter += 1
print("All the files to be converted: ")
print(convert_file_list)
print("=============================================================")

counter = 0
for content in convert_file_list:
    # Get file name
    file_name = os.path.basename(convert_file_list[counter])

    # change directory
    current_directory = os.path.dirname(os.path.abspath("__file__"))
    subprocess.call(["cd", current_directory], shell=True)

    # converting capture format
    infile = convert_file_list[counter]
    outfile = "./output/" + file_name + "_output.cap"
    subprocess.call(["editcap", "-F", "ngwsniffer_2_0", infile, outfile],
                    shell=False)
    print("File <" + file_name + "> has been converted into Sniffer 2.00x format!")
    print("*************************************************************")
    counter += 1
