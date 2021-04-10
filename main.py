import numpy as np
import fnmatch
import os



base_dir = r'C:\Users\Sergej Grischagin\Desktop\40kVs'

#pattern '*_0_????' + '.' + suffix
def replace_sign(dir, replace, replace_with):
    for file in os.listdir(dir):
        if "blah" in file:
            continue

        if file contains '_0_':
            replace '_0_' with '_flats_'



def separate_suffix(filename):
    split_list = filename.split('.')
    if len(split_list) > 1:
        suffix = split_list[-1]
        return filename[:-(len(suffix)+1)], suffix
    else:
        return filename, ''



def main():
    replace_sign(base_dir, replace='_0000_', replace_with='4mm_8mm')


if __name__ == '__main__':
    main()


