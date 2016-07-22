import FileWriter

data = b'\x00\x05\x36\x3e\x74\x79\x1e\x85'

result = data[0] + data[1] * 256 + data[2] * 256 * 256 + data[3] * 256 * 256 * 256 + \
         data[4] * 256 * 256 * 256 * 256 + \
         data[5] * 256 * 256 * 256 * 256 * 256 + \
         data[6] * 256 * 256 * 256 * 256 * 256 * 256 + \
         data[7] * 256 * 256 * 256 * 256 * 256 * 256 * 256

print(result)

t1 = b'\x88\x8d\x02\x1f'
t2 = b'\x45\xf0\x07\x00'

print(FileWriter.little_endian_to_int(t1))
print(FileWriter.little_endian_to_int(t2))
