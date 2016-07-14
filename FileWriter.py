import struct

'''
package 数据结构：
    0: file_name
    1: time_stamp
    2: pkt_counter
    3: content_length
    4: first_pkt_time
    5: first_pkt_length
    6: content
'''


def file_writer(content, timestamp, file_name):
    outfile = "./output/" + file_name + "_output.cap"
    file = open(outfile, "wb")

    head = b'\x58\x43\x50\x00'
    version = b'\x30\x30\x32\x2e\x30\x30\x31\x00'
    if timestamp == "":
        time_stamp = b'\x00\x00\x00\x00'
    else:
        time_stamp = timestamp
    file_length = b''
    first_pkt_time = b''
    first_pkt_length = b''
    pkt_num = b'\x4f\x00\x00\x00'
    dump_00 = b'\x00\x00\x00\x00'
    dump_80 = b'\x80\x00\x00\x00'
    capture = head + version + time_stamp + pkt_num + dump_00 + dump_80 + file_length
    capture = capture + dump_00 * 24 + first_pkt_time + dump_00 + first_pkt_length * 2 + dump_00 * 7
    capture += content

    print("Reverse Test:")
    # print(bytes().fromhex('0102'))
    # print(struct.pack('<H', 65534) + b'\x00\x00')
    # print(struct.pack('<HH', 65534, 1))
    # temp = hex(79)
    # print(repr(temp))
    # temp = hex(79)[2::]
    # print(temp)
    # print(bytes().fromhex(temp))
    # temp += "000000"
    # data = bytes().fromhex(temp)
    # print(temp)
    # print(data)
    int_to_little_endian(468)
    int_to_little_endian(122331)

    # print(struct.pack('@hhhh', int(data[0:2], 16), int(data[2:4], 10), int(data[4:6], 10), int(data[6:8], 10)))
    # print(capture)
    file.write(capture)
    file.close()
    return 0


def little_endian_to_int(data):
    reversed_data = data[3] * 16777216 + data[2] * 65536 + data[1] * 256 + data[0]
    return reversed_data


def int_to_little_endian(data):
    if data < 0:
        print("Number of packets error!")
        return False
    elif data < 65536:
        new_data = struct.pack('<H', data) + b'\x00\x00'
    elif data < 65536 * 65536:
        data_high = data % 65536
        data_low = int(data / 65536)
        new_data = struct.pack('<HH', data_high, data_low)
    else:
        print("Too much packets!")
        return False

    print(little_endian_to_int(new_data))

    return new_data
