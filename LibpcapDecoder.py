import FileWriter


def decoder(file_dir_name, file_name):
    file = open(file_dir_name, "rb")
    full_content = file.read()
    content_length = len(full_content)
    print("Size of the packet: " + str(content_length))

    timestamp = full_content[24:28]
    print("Timestamp is: ")
    print(timestamp)

    tag = b'\x48\x74\x74\x70\x2d\x50\x6f\x72\x74\x3a'
    print(tag)
    pointer = 0
    pkt_counter = 0
    for i in full_content:
        if pointer + 10 > content_length:
            print("Reach the end of the file!")
            break
        if full_content[pointer:pointer + 10] == tag:
            pkt_counter += 1
        pointer += 1

    print("Packet Number is: ")
    print(pkt_counter)
    content = full_content[40:content_length]
    first_pkt_time = full_content[28:32]
    first_pkt_length = full_content[32:34]
    first_pkt_length_check = full_content[36:38]
    if first_pkt_length != first_pkt_length_check:
        print("First Packet Length Error!")
    package = [file_name, timestamp, pkt_counter, content_length, first_pkt_time, first_pkt_length, content]
    FileWriter.file_writer(content, timestamp, file_name)
