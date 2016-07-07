import FileWriter


def decoder(file_dir_name, file_name):
    origin_file = open(file_dir_name, "rb")
    origin_file_content = origin_file.read()

    block_type_start = 0
    block_type_end = 4
    block_type = origin_file_content[block_type_start:block_type_end]
    print("$$ Block Type: " + str(block_type))

    block_total_length_start = 4
    block_total_length_end = 8
    block_total_length = origin_file_content[block_total_length_start:block_total_length_end]
    length = block_total_length.decode("utf-8")
    print("$$ Block Total Length: " + str(block_total_length))

    block_body_start = 8
    block_body_end = origin_file_content[8:32].find(block_total_length) + 8
    block_body = origin_file_content[block_body_start:block_body_end]
    print("$$ Block Body: " + str(block_body))

    block_total_length_2_start = block_body_end
    block_total_length_2_end = block_total_length_2_start + 4
    block_total_length_2 = origin_file_content[block_total_length_2_start:block_total_length_2_end]
    print("$$ Block Total Length: " + str(block_total_length_2))
    if block_total_length != block_total_length_2:
        print("Package parse error!")
        return False
    else:
        print("Package parse succeed!")

    device_system = origin_file_content[112:142]
    print("$$ Device System: " + str(device_system))

    length_of_package = len(origin_file_content)
    print(length_of_package)

    end_of_package = length_of_package - 518
    real_content = origin_file_content[211:end_of_package]
    print("Content parsed!")

    block_type = origin_file_content[0:4]
    print(block_type)
    if block_type == int("0x0a", 16):
        print("This is Pcap-NG file!")
    else:
        print("THIS IS NOT A PCAPNG FILE!")

    block_total_length = origin_file_content[4:8]
    print(str(block_total_length))

    section_head_block = origin_file_content[0:46]
    print(section_head_block)

    FileWriter.file_writer(real_content, file_name)

    return True
