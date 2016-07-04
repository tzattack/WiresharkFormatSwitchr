import os


def file_reader(all_file_list, convert_file_list):
    for path, subdirectories, files in os.walk(r'.'):
        for filename in files:
            file = os.path.join(path, filename)
            all_file_list.append(str(file))

    counter = 0
    for file in all_file_list:
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
