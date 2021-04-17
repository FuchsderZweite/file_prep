import os
import glob
import time


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


def move_files(path, condition, target):
    for path, dirs, files in os.walk(path):
        for i in range(len(dirs)):
            new_base = path + '\\' + dirs[i]
            for j in range(len(target)):
                if not os.path.exists(new_base):
                    create_subdirs(new_base)
                else:
                    for file in os.listdir(new_base):
                        if os.listdir(new_base):
                            for k in range(len(condition)):
                                if condition[k] in file:
                                    target_dir = new_base + '\\' + target[k]
                                    old_file_path = os.path.join(new_base, file)
                                    new_file_path = os.path.join(target_dir, file)
                                    os.rename(old_file_path, new_file_path)
                                    while not os.path.exists(new_file_path):
                                        time.sleep(1)
                                        print('waiting for copy process is done.')
                                        print('new_base: ' + new_base)


def create_subdirs(path):
    os.makedirs(path)
    #for subpath, subdir, subfiles in os.walk(path, topdown=True):
    #    for j in range(len(subdir)):
    #        for i in range(len(target)):
    #            target_dir = path + '\\' + subdir[j] + '\\' + target[i]
    #            if not os.path.exists(target_dir):
    #                os.makedirs(target_dir)


def find_match(path, condition, target):
    if len(condition) != len(target):
        print('lists are not equal in size!.')
    else:
        for dir, subdir, files in os.walk(path):
            for i in range(len(condition)):
                for file in files:
                    if condition[i] in file:
                        old_file_path = path + '\\' + file
                        new_file_path = path + '\\' + target[i] + '\\' + file
                        return old_file_path, new_file_path


'''
def move_files(path, condition, target):
    for path, dirs, files in os.walk(path):
        for i in range(len(dirs)):
            new_root = path + '\\' + dirs[i]
            for subpath, subdir, subfiles in os.walk(new_root):
                target_dir = subpath + '\\' + target
                for file in subfiles:
                    for j in range(len(condition)):
                        if condition[j] in file:
                            if not os.path.exists(target_dir):
                                os.makedirs(target_dir)
                            os.rename(subpath + '\\' + file, target_dir + '\\' + file)
'''


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

