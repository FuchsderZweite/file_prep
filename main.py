import numpy as np
import fnmatch
import os



base_dir = r'C:\Users\Sergej Grischagin\Desktop\test_data'




def separate_suffix(filename):
    split_list = filename.split('.')
    if len(split_list) > 1:
        suffix = split_list[-1]
        return filename[:-(len(suffix)+1)], suffix
    else:
        return filename, ''




#pattern '*_0_????' + '.' + suffix
#if file contains '_0_' than replace '_0_' with 'flats'
def rename_file(dir, rep, repw):
    for root, dirs, files in os.walk(".", topdown=False):
        if rep in files:
            files = files.replace(rep, repw)

       # if file contains '_0_':
       #     replace '_0_' with '_flats_'



def main():
    rename_file(base_dir, rep='_0_', repw='_flats_')


if __name__ == '__main__':
    main()


