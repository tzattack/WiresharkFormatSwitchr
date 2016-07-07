import os
import PcapngDecoder
import FileReader

all_file_list = []
convert_file_list = []

FileReader.file_reader(all_file_list, convert_file_list)


def type_check(infile, file_name):
    file_type = os.path.splitext(infile)[1]
    if file_type == ".txt":
        return False
    elif file_type == ".pcapng":
        PcapngDecoder.decoder(infile, file_name)
        return True


def parser(file_list):
    counter = 0
    for f in file_list:
        # Get file name
        file_name = os.path.basename(file_list[counter])

        # converting capture format
        infile = file_list[counter]
        outfile = "./output/" + file_name + "_output.cap"

        flag = type_check(infile, file_name)

        if flag:
            print("File <" + file_name + "> has been converted into Sniffer 2.00x format!")
            print("*************************************************************")
        counter += 1
    return 0


parser(convert_file_list)
