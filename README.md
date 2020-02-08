# Rename Files

Recursively rename files on a given `path` subtracting from the name a provided string, having a cleaning function on file names.

## USAGE:
	rename_files.py <PATH> <garbage_string>
    PATH - an absolute or relative path
    garbage_string - a part of the filename that have to be deleted.
    
    Pay attention to garbage_string provided!! All occurrences will be
    completely erased from the name of the file regardless of
    their position in the name.

This is the `testbed`:

    testbed
        ├── alfa.txt
        ├── apple.txt
        ├── applegood.txt
        ├── badgoodapple.txt
        ├── beta.txt
        ├── goodapple.txt
        └── goodbetagood.txt

Calling the program:

    ./rename_files.py ./testbed good
    ./rename_files.py testbed/ good
    ./rename_files.py testbed good

The test result without really changing any name:

    Short filename is goodapple.txt
    Old name ./testbed/goodapple.txt contains good so will be changed.
    New name will be ./testbed/apple.txt.
    The file ./testbed/apple.txt already exist and stays unchanged.
    The file ./testbed/goodapple.txt was renamed as ./testbed/kXTCP_apple.txt
    Short filename is badgoodapple.txt
    Old name ./testbed/badgoodapple.txt contains good so will be changed.
    New name will be ./testbed/badapple.txt.
    ./testbed/badgoodapple.txt was renamed ./testbed/badapple.txt
    Short filename is beta.txt
    Short filename is goodbetagood.txt
    Old name ./testbed/goodbetagood.txt contains good so will be changed.
    New name will be ./testbed/beta.txt.
    The file ./testbed/beta.txt already exist and stays unchanged.
    The file ./testbed/goodbetagood.txt was renamed as ./testbed/QbxUq_beta.txt
    Short filename is applegood.txt
    Old name ./testbed/applegood.txt contains good so will be changed.
    New name will be ./testbed/apple.txt.
    The file ./testbed/apple.txt already exist and stays unchanged.
    The file ./testbed/applegood.txt was renamed as ./testbed/gKIVU_apple.txt
    Short filename is apple.txt
    Short filename is alfa.txt

Until otherwise specified this is only a test project.
 
### TO DO:
- rewrite to use pathlike object from pathlib to be more portable.

### testing branch
This is a comment in `testing` branch.

New comment in `testing` after `master` and `dev` diverged.