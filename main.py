import os

base_dir = r'/home/sergej/Desktop/abc/'


def separate_suffix(filename):
    split_list = filename.split('.')
    if len(split_list) > 1:
        suffix = split_list[-1]
        return filename[:-(len(suffix)+1)], suffix
    else:
        return filename, ''


def rename_file(dir, rep, repw):
    n = 0
    for subdir, dirs, files in os.walk(dir):
        for file in files:
            if rep in file:
                n += 1
                new_file = file.replace(rep, repw, 1)
                os.rename(os.path.join(subdir, file), os.path.join(subdir, new_file))
                print(new_file)
    if 0 < n:
        print(f'Done. {n} files were renamed.')
    else:
        print(f'No {rep} were found. Are you sure you spelled {rep} correct? Also check base directory.')



def main():
    rename_file(base_dir, rep='GFK', repw='TEST')


if __name__ == '__main__':
    main()


