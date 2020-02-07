#!/usr/bin/env python3
'''
02.02.2020 - 20:57 - CCR
Search in filenames for a given PATH and deletes garbage
string from them.
Renames the files with the new, cleaned, name testing for
not accidentally overwritting an existing file.

Pay attention to garbage_string provided!! All occurrences will be
completely erased from the name of the file regardless of
their position in the name.
'''

import os, sys, random, string
from pathlib import Path

# 3 arguments has to be provided - the first sys.argv[0] is the program itself
if len(sys.argv) != 3:
    print(
        '''
    USAGE:
    rename_files.py <PATH> <garbage_string>
    PATH - an absolute or relative path
    garbage_string - a part of the filename that have to be deleted.
    
    Pay attention to garbage_string provided!! All occurrences will be
    completely erased from the name of the file regardless of
    their position in the name.
    '''
    )
    sys.exit()
else:
    scan_path = sys.argv[1]
    garbage_string = sys.argv[2]

# A function that generates a random string of variable length
# The characters in the string does not repeat.
def rnd_str(str_length=5):
    word = string.ascii_letters
    return ''.join(random.sample(word,str_length))

# Scans recursively for files in the scan_path
for (dirpath, dirnames, filenames) in os.walk(scan_path):
    for f in filenames:
        old_name = os.path.join(dirpath,f)
        print(f"Short filename is {f}")

        # test if the filename contains garbage_string
        if garbage_string in old_name:
            print(f"The file {old_name} contains the string {garbage_string} so will be changed.")
            # subtract the garbage_string from old_name in new_name
            new_name = old_name.replace(garbage_string, '')
            print(f"New name will be {new_name}.")
        
            # Test if a file with new_name exist already
            if Path(new_name).is_file():
                print(f"The file {new_name} already exist and stays unchanged.")
                # generate a final_name with a random 5 string at start
                final_name = os.path.join(dirpath, rnd_str() + "_" + f.replace(garbage_string, ''))
                print(f"The file {old_name} was renamed as {final_name}")
                #os.renames(old_name, final_name)
            else:
                # if a file with name new_name does not exist
                print(f"{old_name} was renamed {new_name}")
                #os.renames(old_name, new_name)
sys.exit()
          
