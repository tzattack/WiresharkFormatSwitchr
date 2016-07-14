import FileWriter


def decoder(file_dir_name, file_name):
    file = open(file_dir_name, "rb")
    full_content = file.read()
    length = len(full_content)
    print("Size of the packet: " + str(length))

    timestamp = full_content[24:28]
    print("Timestamp is: ")
    print(timestamp)

    tag = b'\x48\x74\x74\x70\x2d\x50\x6f\x72\x74\x3a'
    print(tag)
    pointer = 24
    counter = 0
    for i in full_content:
        print("************************************************")

        counter += 1
        print("No." + str(counter) + " packet: ")
        ts_sec = full_content[pointer:pointer + 4]
        ts_usec = full_content[pointer + 4:pointer + 8]
        incl_len = full_content[pointer + 8:pointer + 12]
        orig_len = full_content[pointer + 12:pointer + 16]
        if incl_len != orig_len:
            print("Exception!")
            break

        pkt_length = FileWriter.little_endian_to_int(incl_len)
        print("\tPacket Length is: " + str(pkt_length))
        pkt_content = full_content[pointer + 12:pointer + 12 + pkt_length]
        pointer = pointer + 12 + pkt_length
        counter += 1
        dump = b'\x00\x00\x00\x00'
        dup_len = full_content[pointer + 8:pointer + 10]
        content = ts_usec + dump + dup_len + dup_len + dump * 7 + pkt_content

    pkt_counter = FileWriter.int_to_little_endian(79)
    print("Packet Number: ")
    print(pkt_counter)
    content = full_content[40:length]
    content_length = FileWriter.int_to_little_endian(length + 2000)
    print("Content Length: ")
    print(content_length)
    print(FileWriter.little_endian_to_int(content_length))
    print(FileWriter.little_endian_to_int(b'\x59\x48\x00\x00'))
    first_pkt_time = full_content[28:32]
    first_pkt_length = full_content[32:34]
    first_pkt_length_check = full_content[36:38]
    if first_pkt_length != first_pkt_length_check:
        print("First Packet Length Error!")

    package = [file_name, timestamp, pkt_counter, content_length, first_pkt_time, first_pkt_length, content]

    FileWriter.file_writer(package)
