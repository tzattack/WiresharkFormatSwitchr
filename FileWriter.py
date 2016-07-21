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


def file_writer(package):
    # 获取解码库所得数据：
    file_name = package[0]
    time_stamp = package[1]
    pkt_counter = package[2]
    content_length = package[3]
    content = package[4]

    # 输出文件地址和文件名：
    outfile = "./output/" + file_name + "_output.cap"
    file = open(outfile, "wb")

    # NA Sniffer Windows 2.00x 文件格式：
    head = b'\x58\x43\x50\x00'
    version = b'\x30\x30\x32\x2e\x30\x30\x31\x00'
    dump_00 = b'\x00\x00\x00\x00'
    dump_80 = b'\x80\x00\x00\x00'
    capture = head + version + time_stamp + pkt_counter + dump_00 + dump_80 + content_length
    capture = capture + dump_00 * 24 + content

    '''
    print("Reverse Test:")
    for i in range(0, 65536 * 66536 - 1):
        if i != little_endian_to_int(int_to_little_endian(i)):
            print("Number: " + str(i))
            print("\tError!")
            break
    print("Success!")
    '''
    # 写入文件
    file.write(capture)
    file.close()
    return 0


# 小端序列转换为整数
def little_endian_to_int(data):
    reversed_data = data[3] * 16777216 + data[2] * 65536 + data[1] * 256 + data[0]
    return reversed_data


# 整数转换为小端序列
def int_to_little_endian(data):
    if data < 0:
        print("Number of packets error!")
        return 0
    elif data < 65536:
        new_data = struct.pack('<H', data) + b'\x00\x00'
    elif data < 65536 * 65536:
        data_high = data % 65536
        data_low = int(data / 65536)
        new_data = struct.pack('<HH', data_high, data_low)
    else:
        print("Too much packets!")
        return 0

    return new_data
