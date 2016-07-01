class pcap_hdr_s:
    magic_number = 0
    version_major = 0
    version_minor = 0
    thiszone = 0
    sigfigs = 0
    snaplen = 0
    network = 0


origin_file = open("test.pcapng", "rb")
origin_file_content = origin_file.read()

block_type_start = 0
block_typr_end = 4
block_type = origin_file_content[block_type_start:block_typr_end]
print("$$ Block Type: " + str(block_type))

block_total_length_start = 4
block_total_length_end = 8
block_total_length = origin_file_content[block_total_length_start:block_total_length_end]
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
else:
    print("Package parse succeed!")