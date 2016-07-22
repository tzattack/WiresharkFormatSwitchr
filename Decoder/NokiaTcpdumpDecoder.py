import FileWriter
import struct


def decoder(file_dir_name, file_name):
    # open file
    file = open(file_dir_name, "rb")
    full_content = file.read()
    length = len(full_content)
    print("Size of the packet: " + str(length))

    pointer = 0  # point to the location where the packet is parsed
    number = 0  # number of packets
    dump = b'\x00\x00\x00\x00'
    content = b''

    pointer += 24

    for i in full_content:
        if pointer >= length:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("Reach the end of the file!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            break

        number += 1
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Packet NO," + str(number))

        original_length = full_content[pointer + 8:pointer + 12]
        included_length = full_content[pointer + 12:pointer + 16]
        print("included: " + str(included_length))

        timestamp_seconds = full_content[pointer:pointer + 4]
        timestamp_microseconds = full_content[pointer + 4:pointer + 8]

        data_length = FileWriter.little_endian_to_int(included_length)
        print("\tData length: " + str(data_length))
        packet_data = full_content[pointer + 20:pointer + 20 + data_length]

        dup_len = struct.pack('<H', data_length)
        print("\tDuplex length: " + str(dup_len))

        if number == 1:
            orgin_time = timestamp_seconds
            time_stamp = timestamp_seconds

        time_base = FileWriter.little_endian_to_int(timestamp_seconds) * 1000000 + FileWriter.little_endian_to_int(
            timestamp_microseconds)
        time_to_add = time_base - FileWriter.little_endian_to_int(orgin_time) * 1000000
        print("\tTime to add: " + str(time_to_add))
        time_plus = FileWriter.int_to_little_endian(time_to_add)

        content += time_plus + dump + dup_len + dup_len + dump * 7 + packet_data

        pointer = pointer + data_length + 20

    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$")
    pkt_counter = FileWriter.int_to_little_endian(number)

    temp_length = len(content)
    content_length = FileWriter.int_to_little_endian(temp_length + 128)
    print("\tContent Length: " + str(FileWriter.little_endian_to_int(content_length)))
    print("\tExpected Length: " + str(FileWriter.little_endian_to_int(b'\x59\x48\x00\x00')))
    print("\tOrigin Time: " + str(FileWriter.little_endian_to_int(time_stamp)))

    package = [file_name, time_stamp, pkt_counter, content_length, content]

    FileWriter.file_writer(package)

    return True
