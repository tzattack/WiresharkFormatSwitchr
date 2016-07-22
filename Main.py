import os
import PcapngDecoder
import LibpcapDecoder
import SnoopDecoder
import NanosecondLibpcapDecoder
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
    elif file_type == ".pcap":
        file_check(infile, file_name)
        return True
    elif file_type == ".snoop":
        SnoopDecoder.decoder(infile, file_name)
    else:
        print("<" + file_name + "> Unknown File Format!")
        return False


def file_check(infile, file_name):
    # open file
    file = open(infile, "rb")
    full_content = file.read()

    if full_content[0:8] == b'\x4d\x3c\xb2\xa1\x02\x00\x04\x00':
        print("<" + file_name + "> is NanosecondLibpcap File")
        NanosecondLibpcapDecoder.decoder(infile, file_name)
        return True
    elif full_content[0:8] == b'\x4d\x3c\xb2\xa1\x02\x00\x04\x00':
        print("<" + file_name + "> is Libpcap File")
        LibpcapDecoder.decoder(infile, file_name)
    elif full_content[0:8] == b'\x34\xcd\xb2\xa1\x02\x00\x04\x00':
        print("<" + file_name + "> is Modified Tcpdump File")
        LibpcapDecoder.decoder(infile, file_name)
    else:
        print("<" + file_name + "> is Unknown File Format!")
        return False


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
