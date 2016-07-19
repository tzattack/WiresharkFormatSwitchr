import FileWriter


def decoder(file_dir_name, file_name):
    file = open(file_dir_name, "rb")
    full_content = file.read()
    length = len(full_content)
    orig_time = full_content[24:28]
    print("Size of the packet: " + str(length))

    time_stamp = orig_time
    print("Timestamp is: ")
    print(time_stamp)

    tag = b'\x48\x74\x74\x70\x2d\x50\x6f\x72\x74\x3a'
    print(tag)
    pointer = 24
    counter = 1
    content = b''
    for i in full_content:
        print("************************************************")

        if pointer >= length:
            print("Reach the end of the file!")
            break
        print("No." + str(counter) + " packet: ")
        ts_sec = full_content[pointer:pointer + 4]
        print("\tTime sec is: " + str(ts_sec))
        ts_usec = full_content[pointer + 4:pointer + 8]
        print("\tTime microsec is: " + str(ts_usec))
        incl_len = full_content[pointer + 8:pointer + 12]
        print("\tNumber of octects of packet saved in file: " + str(incl_len))
        orig_len = full_content[pointer + 12:pointer + 16]
        print("\tActual length of packet: " + str(orig_len))
        dup_len = full_content[pointer + 8:pointer + 10]
        if FileWriter.little_endian_to_int(incl_len) > FileWriter.little_endian_to_int(orig_len):
            print("Packet Length Exception!")
            break

        pkt_length = FileWriter.little_endian_to_int(incl_len)
        print("\tPacket Length is: " + str(pkt_length))
        pkt_content = full_content[pointer + 16:pointer + 16 + pkt_length]
        pointer = pointer + 16 + pkt_length
        counter += 1
        dump = b'\x00\x00\x00\x00'
        print(FileWriter.little_endian_to_int(ts_sec))
        print(FileWriter.little_endian_to_int(ts_usec))
        time_base = FileWriter.little_endian_to_int(ts_sec) * 1000000 + FileWriter.little_endian_to_int(ts_usec)
        time_to_add = time_base - FileWriter.little_endian_to_int(orig_time) * 1000000
        print("Time to add: " + str(time_to_add))
        time_plus = FileWriter.int_to_little_endian(time_to_add)
        print(time_plus)
        content += time_plus + dump + dup_len + dup_len + dump * 7 + pkt_content

    pkt_counter = FileWriter.int_to_little_endian(79)
    print("Packet Number: ")
    print(pkt_counter)
    temp_length = len(content)
    content_length = FileWriter.int_to_little_endian(temp_length + 128)
    print("Content Length: ")
    print(FileWriter.little_endian_to_int(content_length))
    print(FileWriter.little_endian_to_int(b'\x59\x48\x00\x00'))
    print("Origin Time: " + str(FileWriter.little_endian_to_int(time_stamp)))

    package = [file_name, time_stamp, pkt_counter, content_length, content]

    FileWriter.file_writer(package)
