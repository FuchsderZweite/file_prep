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


def logging(path, filename):
    log_c = 0
    today = datetime.date.today()
    f = open(dir + '\\REMOVED_FILES_log.txt', 'a+')
    if log_c == 0:
        f.write('\n\n')
        f.write('==========\t' + f'{today}' + '\t==========\n')
    f.write('removed\t' + f'{filename}' + '\tfrom dir\t' + path + '\n')
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

    remove_file(base_dir, rm=list_rm, log=True)
    rename_file(path=base_dir, rep=list_rep, repw=list_repw)


if __name__ == '__main__':
    main()




