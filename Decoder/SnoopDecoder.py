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

    identification_pattern = full_content[0:8]
    if identification_pattern != b'\x73\x6e\x6f\x6f\x70\x00\x00\x00':
        print("Unrecognized Snoop File!")
        return False

    version_number = full_content[8:12]
    datalink_type = datalink_type_checker(full_content[12:16])

    pointer += 16
    for i in full_content:
        if pointer >= length:
            print("^^^^^^^^^^^^^^^^^^^^^^^^^^^")
            print("Reach the end of the file!")
            print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
            break

        number += 1
        print("++++++++++++++++++++++++++++++++++++++++++++++++")
        print("Packet NO," + str(number))

        original_length = full_content[pointer:pointer + 4]
        included_length = full_content[pointer + 4:pointer + 8]
        packet_record_length = full_content[pointer + 8:pointer + 12]
        packet_record_length_int = packet_record_length[0] * 16777216 + packet_record_length[1] * 65536 + \
                                   packet_record_length[2] * 256 + packet_record_length[3]
        cumulative_drops = full_content[pointer + 12:pointer + 16]
        timestamp_seconds = full_content[pointer + 16:pointer + 20]
        timestamp_microseconds = full_content[pointer + 20:pointer + 24]
        data_length = included_length[0] * 16777216 + included_length[1] * 65536 + included_length[2] * 256 + \
                      included_length[3]
        print("\tData length: " + str(data_length))
        packet_data = full_content[pointer + 24:pointer + 24 + data_length]

        dup_len = struct.pack('<H', data_length)
        print("\tDuplex length: " + str(dup_len))

        time_high = timestamp_seconds[0] * 16777216 + timestamp_seconds[1] * 65536 + timestamp_seconds[2] * 256 + \
                    timestamp_seconds[3]
        time_low = timestamp_microseconds[0] * 16777216 + timestamp_microseconds[1] * 65536 + timestamp_microseconds[
                                                                                                  2] * 256 + \
                   timestamp_microseconds[3]
        if number == 1:
            orgin_time = time_high
            time_stamp = FileWriter.int_to_little_endian(orgin_time)

        time_base = time_high * 1000000 + time_low
        time_to_add = time_base - orgin_time * 1000000
        print("\tTime to add: " + str(time_to_add))
        time_plus = FileWriter.int_to_little_endian(time_to_add)

        content += time_plus + dump + dup_len + dup_len + dump * 7 + packet_data

        pointer += packet_record_length_int

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


def datalink_type_checker(content):
    if content == 0:
        return "IEEE 802.3"
    elif content == 1:
        return "IEEE 802.4 Token Bus"
    elif content == 2:
        return "IEEE 802.5 Token Ring"
    elif content == 3:
        return "IEEE 802.6 Metro Net"
    elif content == 4:
        return "Ethernet"
    elif content == 5:
        return "HDLC"
    elif content == 6:
        return "Character Synchronous"
    elif content == 7:
        return "IBM Channel-to-Channel"
    elif content == 8:
        return "FDDI"
    elif content == 9:
        return "Other"
    else:
        return "Unassigned"