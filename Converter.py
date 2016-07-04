import os
import subprocess
import PcapngDecoder

'''
Loading all file list
'''
all_file_list = []
for path, subdirectories, files in os.walk(r'.'):
    for filename in files:
        file = os.path.join(path, filename)
        all_file_list.append(str(file))

'''
pcapng file converting
'''
counter = 0
convert_file_list = []
for convert_file in all_file_list:
    if all_file_list[counter].find(".snoop") is not -1:
        convert_file = all_file_list[counter]
        convert_file_list.append(convert_file)
    elif all_file_list[counter].find(".pcap") is not -1:
        convert_file = all_file_list[counter]
        convert_file_list.append(convert_file)
    elif all_file_list[counter].find(".cap") is not -1:
        convert_file = all_file_list[counter]
        convert_file_list.append(convert_file)
    elif all_file_list[counter].find(".libpcap") is not -1:
        convert_file = all_file_list[counter]
        convert_file_list.append(convert_file)
    elif all_file_list[counter].find(".5vw") is not -1:
        convert_file = all_file_list[counter]
        convert_file_list.append(convert_file)
    elif all_file_list[counter].find(".txt") is not -1:
        convert_file = all_file_list[counter]
        convert_file_list.append(convert_file)
    elif all_file_list[counter].find(".ncf") is not -1:
        convert_file = all_file_list[counter]
        convert_file_list.append(convert_file)
    counter += 1
print("All the files to be converted: ")
print(convert_file_list)
print("=============================================================")


def type_check(infile):
    file_type = os.path.splitext(infile)[1]
    if file_type == ".txt":
        decode_txt()
    elif file_type == ".pcapng":
        PcapngDecoder.decode_pcapng(infile)
    return 0


counter = 0
for content in convert_file_list:
    # Get file name
    file_name = os.path.basename(convert_file_list[counter])

    # change directory
    current_directory = os.path.dirname(os.path.abspath("__file__"))

    # converting capture format
    infile = convert_file_list[counter]
    outfile = "./output/" + file_name + "_output.cap"

    type_check(infile)

    print("File <" + file_name + "> has been converted into Sniffer 2.00x format!")
    print("*************************************************************")
    counter += 1


def decode_txt():
    return 0
