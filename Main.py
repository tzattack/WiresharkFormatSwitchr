import os

import Decoder.LibpcapDecoder
import Decoder.ModifiedTcpdumpDecoder
import Decoder.PcapngDecoder
import Decoder.SnoopDecoder
import Decoder.NokiaTcpdumpDecoder
import Decoder.NanosecondLibpcapDecoder
import Decoder.RedHatTcpdumpDecoder

import FileReader

all_file_list = []
convert_file_list = []

FileReader.file_reader(all_file_list, convert_file_list)


def type_check(infile, file_name):
    file_type = os.path.splitext(infile)[1]
    if file_type == ".txt":
        return False
    elif file_type == ".pcapng":
        Decoder.PcapngDecoder.decoder(infile, file_name)
        return True
    elif file_type == ".pcap":
        file_check(infile, file_name)
        return True
    elif file_type == ".snoop":
        Decoder.SnoopDecoder.decoder(infile, file_name)
    else:
        print("<" + file_name + "> Unknown File Format!")
        return False


def file_check(infile, file_name):
    # open file
    file = open(infile, "rb")
    full_content = file.read()

    if full_content[0:8] == b'\x4d\x3c\xb2\xa1\x02\x00\x04\x00':
        print("<" + file_name + "> is NanosecondLibpcap File")
        Decoder.NanosecondLibpcapDecoder.decoder(infile, file_name)
        return True
    elif full_content[0:8] == b'\xd4\xc3\xb2\xa1\x02\x00\x04\x00':
        if full_content[40:44] != b'\x00\x00\x00\x00':
            print("<" + file_name + "> is Libpcap File")
            Decoder.LibpcapDecoder.decoder(infile, file_name)
        elif full_content[40:48] != b'\x00\x00\x00\x00\x00\x00\x00\x00':
            print("<" + file_name + "> is Nokia Tcpdump File")
            Decoder.NokiaTcpdumpDecoder.decoder(infile, file_name)
        elif full_content[40:48] == b'\x00\x00\x00\x00\x00\x00\x00\x00':
            print("<" + file_name + "> is Redhat Tcpdump File")
            Decoder.RedHatTcpdumpDecoder.decoder(infile, file_name)
    elif full_content[0:8] == b'\x34\xcd\xb2\xa1\x02\x00\x04\x00':
        if full_content[48:52] != b'\x00\x00\x00\x00':
            print("<" + file_name + "> is Modified Tcpdump File")
            Decoder.ModifiedTcpdumpDecoder.decoder(infile, file_name)
        elif full_content[48:52] == b'\x00\x00\x00\x00':
            print("<" + file_name + "> is SuSE Tcpdump File")
            Decoder.SeSETcpdumpDecoder.decoder(infile, file_name)
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
