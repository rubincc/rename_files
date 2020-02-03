#!/usr/bin/env python3
'''
02.02.2020 - 20:57 - CCR
Search in filenames for a given PATH and deletes garbage
string from them.
Renames the files with the new, cleaned, name.

Pay attention to garbage_string provided!! All occurrences will be
completely erased from the name of the file regardless of
their position in the name.
'''

import os, sys
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
    
# Scans recursively for files in the scan_path
for (dirpath, dirnames, filenames) in os.walk(scan_path):
    for f in filenames:
        old_name = os.path.join(dirpath,f)
        new_name = old_string.replace(garbage_string, '')
        
        # renames the files with cleaned names
        if Path(new_string).is_file():
            print(f"The file {new_name} exist already. Did nothing.")
        else:
            os.renames(old_name, new_name)
            print("The file {0} was renamed as {1}".format(old_name, new_name))


