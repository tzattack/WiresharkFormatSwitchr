import FileWriter
import struct


def decoder(file_dir_name, file_name):
    # open file
    file = open(file_dir_name, "rb")
    full_content = file.read()
    length = len(full_content)
    print("Size of the packet: " + str(length))

    pointer = 0  # point to the location where the packet is parsed
    counter = 0  # count the number of the block in the packet
    number = 0  # number of packets
    dump = b'\x00\x00\x00\x00'
    content = b''

    # parsing the packet
    for b in full_content:
        print("----------------------------")
        if pointer >= length:  # in case of reaching the end of the file
            print("Reach the end of the file!!!")
            break
        block_type = full_content[pointer:pointer + 4]  # block type
        counter += 1
        print("No." + str(counter) + " Block: ")
        flag = block_checker(block_type)  # whether the block is useful
        block_length = int(
            FileWriter.little_endian_to_int(full_content[pointer + 4:pointer + 8]))  # the length of the block
        print("\tBlock Length: " + str(block_length))
        capture_len = FileWriter.little_endian_to_int(full_content[pointer + 20:pointer + 24])
        print("\tCapture length: " + str(capture_len))

        time_stamp = full_content[pointer + 12: pointer + 20]
        # check the parsing result is correspond to what we expected
        if full_content[pointer + 4:pointer + 8] != full_content[pointer + block_length - 4:pointer + block_length]:
            print("Block parse error!")
        else:
            print("Block parse succeed!")

        # output useful information
        if flag == 1:
            number += 1

            if number == 1:
                orig_time = time_stamp
                print("Origin Time: ")
                print(bit_64_hex_to_int(orig_time))

            pkt_content = full_content[pointer + 28:pointer + 28 + capture_len]

            dup_len = struct.pack('<h', capture_len)
            print("Duplex length: " + str(dup_len))

            time_base = orig_time
            time_to_add = bit_64_hex_to_int(time_stamp) - bit_64_hex_to_int(time_base)
            time_plus = FileWriter.int_to_little_endian(time_to_add)
            print("Time to add: " + str(time_to_add))
            print("Time stamp: " + str(bit_64_hex_to_int(time_stamp)))

            content += orig_time + dump + dup_len + dup_len + dump * 7 + pkt_content

            print("Timestamp is: " + str(time_stamp))
            print("Collected position: " + str(pointer + block_length))

        # move pointer
        pointer += block_length
        print("Pointer now: " + str(pointer))
        temp_length = len(content)
        content_length = FileWriter.int_to_little_endian(temp_length + 128)

    print("The number of packets: " + str(number))

    print("Content Length: " + str(FileWriter.little_endian_to_int(content_length)))
    print("Target Length: " + str(FileWriter.little_endian_to_int(b'\x59\x48\x00\x00')))

    pkt_counter = FileWriter.int_to_little_endian(number)
    package = [file_name, orig_time, pkt_counter, content_length, content]
    FileWriter.file_writer(package)

    print("TESTTTTT: ")
    print(bit_8_hex_to_int(b'\xff'))

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


def bit_8_hex_to_int(data):
    res = data[0]
    return res


def bit_64_hex_to_int(data):
    res = data[4] + data[5] * 16 + data[6] * 256 + data[7] * 4096 + data[0] * 65536 + data[1] * 1048576 + data[
                                                                                                              2] * 16777216 + \
          data[3] * 268435456
    return res
