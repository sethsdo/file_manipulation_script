# Title: File Manipulation Script
# Author: Seth Olmstead
# PY Version: 3.7.0
# ex run steps:
  # 1 - open folder
  # 2 - run: python modify.py smb.txt “password sync = yes” “password sync = no” 

import sys
import os.path

file_spec    = sys.argv[1]              # read file name of from first arg
search_text  = sys.argv[2]              # text to search for
replace_text = sys.argv[3]              # text to replace with

if os.path.exists(file_spec):           # check if file exists

    out_file    = os.path.splitext(file_spec)[0] + '.new.txt'    # write file with new appended to title
    out_pointer = open(out_file, 'w')                            # open write file
    in_pointer  = open(file_spec, 'r')                           # open read file

    lines_updated  = 0   # track updated lines
    text_occurrence = 0  # track updated text

    for line in in_pointer.readlines():     # loop through all file lines
        if line.find(search_text) != -1:
            new_ln = line.replace(search_text, replace_text)  # store updated line in variable
            out_pointer.write(new_ln)                         # replace old text with newclear
            text_occurrence += line.count(search_text)        # increment occurrence of replaced text
            lines_updated += 1                                # increment updated lines count
        else:
            out_pointer.write(line)

    # close file
    in_pointer.close() 
    out_pointer.close()

    file_spec + '.bak'                                        # append extention
    new_path = './processed/' + file_spec                     # new file path  
    os.rename(os.path.abspath(file_spec), new_path)           # move file to new location


    print('Lines where updated.', lines_updated)
    print('Text Occurrences replaced: ', lines_updated)
else:
    print("Error: File not found.")



# Put your code here
input_file = input('Enter an input filename: ')
output_file = input('Enter a output filename: ')

in_f = open(input_file, "r")
out_f = open(output_file, 'w+')

count = 0
for line in in_f:
    count+=1
    out_f.write('%4s %6s' % (str(count), str(line)))