import os
import glob
import time
import datetime


def separate_suffix(filename):
    split_list = filename.split('.')
    if len(split_list) > 1:
        suffix = split_list[-1]
        return filename[:-(len(suffix)+1)], suffix
    else:
        return filename, ''


def remove_file(dir, rm, log):
    for dir, subdirs, files in os.walk(dir):
        for k in range(len(subdirs)):
            _dir = os.path.join(dir, subdirs[k])
            for file in os.listdir(_dir):
                for _r in rm:
                    if _r in file:
                        os.remove(os.path.join(_dir, file))
                        if log:
                            logging(_dir, file)


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


def logging(path, filename):
    log_file_dir = r'\\132.187.193.8\junk\sgrischagin'
    log_c = 0
    today = datetime.date.today()
    f = open(log_file_dir + '\\REMOVED_FILES_log.txt', 'a+')
    if log_c == 0:
        f.write('\n\n')
        f.write('==========\t' + f'{today}' + '\t==========\n')
    f.write('REMOVED\t' + f'{filename}' + '\tFROM DIR\t' + path + '\n')
    f.close()
    log_c += 1


def move_n_sort(path, filter, condition, target):
    count = 0
    path_refs = None
    _subdir_img = None
    fin = False
    for dir in os.listdir(path):
        if os.path.isdir(os.path.join(path, dir)) and dir != 'darks' and dir != 'refs':
            _dir = os.path.join(path, dir)
            if not os.path.exists(os.path.join(_dir, 'imgs')):
                create_subdirs(os.path.join(_dir, 'imgs'))
            if not os.path.exists(os.path.join(_dir, 'refs')):
                create_subdirs(os.path.join(_dir, 'refs'))
            path_refs = os.path.join(_dir, 'refs')
            _subdir_img = os.path.join(_dir, 'imgs')
            for _f in filter:
                if not os.path.exists(os.path.join(_subdir_img, _f)):
                    create_subdirs(os.path.join(_subdir_img, _f))
                    _subsubdir_img = os.path.join(_subdir_img, _f)
                for _a in range(1, len(target)):
                    if not os.path.exists(os.path.join(_subdir_img, _f, target[_a])):
                        create_subdirs(os.path.join(_subdir_img, _f, target[_a]))

        for file in os.listdir(_dir):
            if condition[0] in file:
                _move_file(os.path.join(_dir, file), os.path.join(path_refs, file))
            else:
                for f in filter:
                    if f in file:
                        for k in range(1, len(condition)):
                            if condition[k] in file:
                                print(f'condition match!{dir} - {file}')
                                count += 1
                                _move_file(os.path.join(_dir, file) ,os.path.join(_dir, 'imgs', f, target[k], file))
                                while not os.path.exists(os.path.join(_dir, 'imgs', f, target[k])):
                                    time.sleep(100)
                                    print('waiting for copy process is done.')
        if len(dir) == 2:
            fin = True
    if fin:
        print(f'Done. {count} files were moved.')


def _move_file(o_path, n_path):
    old_file_path = os.path.join(o_path)
    new_file_path = os.path.join(n_path)
    os.rename(old_file_path, new_file_path)


def create_subdirs(path):
    os.makedirs(path)


def wait(path, t):
    while not os.path.exists(path):  # faced regularly issues due to working on not existing path (writing to network is slow)
        time.sleep(t)


if __name__ == '__main__':
    start = time.time()
    base_dir = r'\\132.187.193.8\junk\sgrischagin\2021-08-09-Sergej_SNR_Stufelkeil_40-75kV'


    ''' === remove unnecessary data ============================== '''
    list_rm = ['_I0Image', '_DarkImage']
    remove_file(dir=base_dir, rm=list_rm, log=True)
    ''' ========================================================== '''


    ''' ==== moving raw data in specific folder for structure ===  '''
    list_filter = ['_none_', '_1mm Al_', '_2mm Al_']
    # put your relative positions where the projections were made here:
    # Caution! the very first index (list_condition_pos[0]) must be the flat-images position!
    list_condition_pos = ['_-65p00_', '_-46p70_', '_-26p60_', '_-6p55_', '13p55']
    list_target = ['refs', '_1-area_', '_2-area_', '_3-area_', '_4-area_']
    move_n_sort(path=base_dir, filter=list_filter, condition=list_condition_pos, target=list_target)
    '''  ========================================================= '''

    print(f'Time: {(time.time() - start) / 60} min')
