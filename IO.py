import os
import subprocess

'''
Loading all file list
'''
all_file_list = []
for path, subdirectories, files in os.walk(r'.'):
    for filename in files:
        f = os.path.join(path, filename)
        all_file_list.append(str(f))
print("All the files in directory and subdirectory: ")
print(all_file_list)

'''
pcapng file converting
'''
counter = 0
pcapng_file_list = []
for pcapng_file in all_file_list:
    if all_file_list[counter].find(".pcapng") is not -1:
        pcapng_file = all_file_list[counter]
        pcapng_file_list.append(pcapng_file)
    counter += 1
print("All the pcapng file: ")
print(pcapng_file_list)

counter = 0
for content in pcapng_file_list:
    # Get file name
    file_name = os.path.basename(pcapng_file_list[counter])
    print(file_name)
    subprocess.call(["echo", "Hello, world!"], shell=False)
    # change directory
    current_directory = os.path.dirname(os.path.abspath("__file__"))
    print("Current directory is : " + current_directory)
    subprocess.call(["cd", current_directory], shell=True)
    # converting capture format
    script_dir = os.path.dirname(os.path.abspath("__file__"))
    rel_path = file_name
    abs_file_path = os.path.join(script_dir, rel_path)
    infile = pcapng_file_list[counter]
    print("*******Infile directory: " + infile)
    abs_file_output_path = os.path.join(script_dir, ".\output\\")
    output_file_name = "./output/" + file_name + "_output.cap"
    print(output_file_name)
    subprocess.call(["editcap", "-F", "ngwsniffer_2_0", infile, output_file_name],
                    shell=False)

    counter += 1