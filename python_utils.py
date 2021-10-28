"""!
@file       python_utils.py

@brief      Utilities for simple python operations
@author     SachinJayaram
@date       9/2017
"""

import shutil

def copy_file(src, dest):
    """!
    Copy the file from src to dest.

    @param src the source file path.
    @param dest the destination path to copy the file.

    @return return_value success or failure of the copy command.
    """
    return_value = 0
    try:
        shutil.copy(src, dest)
    except shutil.Error as error:
        # Throw an exception if the src and dest are identical
        print(error)
        return_value = 1
    except IOError as err:
        # Throw an exception if the src or dest doesn't exist
        print(error.strerror)
        return_value = error.errno

    return return_value
