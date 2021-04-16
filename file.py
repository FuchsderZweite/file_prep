import os
import glob
import datetime


def separate_suffix(filename):
    split_list = filename.split('.')
    if len(split_list) > 1:
        suffix = split_list[-1]
        return filename[:-(len(suffix)+1)], suffix
    else:
        return filename, ''


def remove_file(dir, rm, log):
    path = glob.glob(dir + '\\*')
    for k in range(len(path)):
        for i in range(len(rm)):
            for root, dirs, files in os.walk(path[k]):
                for file in files:
                    if rm[i] in file:
                        os.remove(os.path.join(path[k], file))
                        if log:
                            logging(path[k], file)

# TODO: move_files!
def move_files(path, condition, target):
    for path, dirs, files in os.walk(path):
        for i in range(len(dirs)):
            new_root = path + '\\' + dirs[i]
            for subpath, subdir, subfiles in os.walk(new_root):
                # check if targets exist here:
                for k in range(len(subdir)):
                    target_dir = new_root + '\\' + target[k]
                    for q in subdir:
                        if not os.path.exists(target_dir):
                            os.makedirs(target_dir)
                        os.rename(new_root + '\\' + target[k], target_dir + '\\' + file)


def create_subdirs(path, target):
    for subpath, subdir, subfiles in os.walk(path, topdown=True):
        for j in range(len(subdir)):
            for i in range(len(target)):
                target_dir = path + '\\' + subdir[j] + '\\' + target[i]
                if not os.path.exists(target_dir):
                    os.makedirs(target_dir)


def create_subdirs2(path, target):

    for subpath, subdir, subfiles in os.walk(path):
        target_dir = path + '\\' + target[i]
        for i in range(len(target)):
            if not os.path.exists(target_dir):
                os.makedirs(target_dir)
                print('created folder in: ' f'{target_dir}.')
            else:
                print('subdir exists already.')


def logging(path, filename):
    log_c = 0
    today = datetime.date.today()
    f = open(dir + '\\REMOVED_FILES_log.txt', 'a+')
    if log_c == 0:
        f.write('\n\n')
        f.write('==========\t' + f'{today}' + '\t==========\n')
    f.write('REMOVED\t' + f'{filename}' + '\tFROM DIR\t' + path + '\n')
    f.close()
    log_c += 1


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
    base_dir = r'.'

    list_rep = ['_0_']
    list_repw = ['_refs_']

    list_rm = ['_DarkImage', '_I0Image']

    list_condition = ['_4u8mm_', '_12u16mm_', '_20u24mm_', '_28u32mm_']
    list_target = ['4u8mm', '12u16mm', '20u24mm', '28u32mm']


if __name__ == '__main__':
    main()
