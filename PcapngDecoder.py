import FileWriter


def decoder(file_dir_name, file_name):
    # open file
    file = open(file_dir_name, "rb")
    full_content = file.read()
    content_length = len(full_content)
    print("Size of the packet: " + str(content_length))

    pointer = 0  # point to the location where the packet is parsed
    counter = 0  # count the number of the block in the packet
    number = 0  # number of packets
    packet_content = b''

    # parsing the packet
    for b in full_content:
        print("----------------------------")
        if pointer >= content_length:  # in case of reaching the end of the file
            break
        block_type = full_content[pointer:pointer + 4]  # block type
        counter += 1
        print("No." + str(counter) + " Block: ")
        flag = block_checker(block_type)  # whether the block is useful
        block_length = int(reverse_binary(full_content[pointer + 4:pointer + 8]))  # the length of the block
        print("\tBlock Length: " + str(block_length))

        timestamp_high = full_content[pointer + 12: pointer + 16]
        timestamp_low = full_content[pointer + 16: pointer + 20]
        # check the parsing result is correspond to what we expected
        if full_content[pointer + 4:pointer + 8] != full_content[pointer + block_length - 4:pointer + block_length]:
            print("Block parse error!")
        else:
            print("Block parse succeed!")
        pointer += block_length
        print("Pointer now: " + str(pointer))

        # output useful information
        if flag == 1:
            packet_content += full_content[pointer - block_length:pointer]
            print("Timestamp is: " + str(timestamp_high) + str(timestamp_low))
            number += 1
            print("Collected position: " + str(pointer))

    print("The number of packets: " + str(number))

    time_stamp = timestamp_high

    FileWriter.file_writer(packet_content, time_stamp, file_name)

    return True


def block_checker(block_type):
    shb_block_type = b'\x0a\x0d\x0d\x0a'
    idb_block_type = b'\x01\x00\x00\x00'
    pb_block_type = b'\x02\x00\x00\x00'
    spb_block_type = b'\x03\x00\x00\x00'
    nrb_block_type = b'\x04\x00\x00\x00'
    isp_block_type = b'\x05\x00\x00\x00'
    epb_block_type = b'\x06\x00\x00\x00'
    irig_block_type = b'\x07\x00\x00\x00'

    if block_type == shb_block_type:
        print("\tSHB parsed!")
        return 0
    elif block_type == idb_block_type:
        print("\tIDB parsed!")
        return 0
    elif block_type == pb_block_type:
        print("\tPB parsed!")
        return 0
    elif block_type == spb_block_type:
        print("\tSPB parsed!")
        return 0
    elif block_type == nrb_block_type:
        print("\tNRB parsed!")
        return 0
    elif block_type == isp_block_type:
        print("\tISP parsed!")
        return 0
    elif block_type == epb_block_type:
        print("\tEPB parsed!")
        return 1
    elif block_type == irig_block_type:
        print("\tIRIG parsed!")
        return 0
    else:
        print("\tUnknown block!")
        return 0


def reverse_binary(data):
    reversed_data = data[3] * 16777216 + data[2] * 65536 + data[1] * 256 + data[0]
    return reversed_data
