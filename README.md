# Rename Files

Recursively rename files on a given __path__ substracting from the name a provided string, having a cleaning function on file names.

## USAGE:
	rename_files.py <PATH> <garbage_string>
    PATH - an absolute or relative path
    garbage_string - a part of the filename that have to be deleted.
    
    Pay attention to garbage_string provided!! All occurrences will be
    completely erased from the name of the file regardless of
    their position in the name.

