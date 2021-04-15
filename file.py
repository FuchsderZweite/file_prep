import os
import glob

def separate_suffix(filename):
    split_list = filename.split('.')
    if len(split_list) > 1:
        suffix = split_list[-1]
        return filename[:-(len(suffix)+1)], suffix
    else:
        return filename, ''






def walklevel(some_dir, level):
    some_dir = some_dir.rstrip(os.path.sep)
    assert os.path.isdir(some_dir)
    num_sep = some_dir.count(os.path.sep)
    for root, dirs, files in os.walk(some_dir):
        yield root, dirs, files
        num_sep_this = root.count(os.path.sep)
        if num_sep + level <= num_sep_this:
            del dirs[:]


'''
def move_files(dir, create_folder, dir_name):
    if create_folder:
        for subdir, dirs, files in os.walk(dir):
            new_folder = subdir + dirs
            if not os.path.exists(new_folder):
                os.makedirs(dir_name)
                os.rename(subdir + dirs + files, subdir + dirs)
    else:
'''


def rename_file(path, rep, repw):
    if len(rep) != len(repw):
        print('the length (its entries) of the passed lists are not equal!')
    else:
        path = glob.glob(path + '\\*')
        n = 0
        for k in range(len(path)):
            for i in range(len(rep)):
                for root, dirs, files in os.walk(path[k]):
                    for file in files:
                        if rep[i] in file:
                            n += 1
                            new_file = file.replace(rep[i], repw[i], 1)
                            os.rename(os.path.join(root, file), os.path.join(root, new_file))
        print('Done...' + f'{n}' + ' files were renamed.')





def main():
    base_dir = r'\\132.187.193.8\junk\sgrischagin\Dritte_Messung'
    #replace = '_00_'
    #replace_with = '_4u8mm_'
    list_rep = ['_00_', '_000_', '_0000_', '_00000_']
    list_repw = ['_4u8mm_', '_12u16mm_', '_20u24mm_', '_28u32mm_']


    rename_file(path=base_dir, rep=list_rep, repw=list_repw)


if __name__ == '__main__':
    main()

