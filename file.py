import os

def separate_suffix(filename):
    split_list = filename.split('.')
    if len(split_list) > 1:
        suffix = split_list[-1]
        return filename[:-(len(suffix)+1)], suffix
    else:
        return filename, ''

def rename_file(dir, rep, repw):
    if isinstance(dir, str) and isinstance(rep, str) and isinstance(repw, str):
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
    else:
        #print(f'No parameter are passed: dir: {dir}, rep: {rep}, repw: {repw}')
        print('passed parameter must be strings!')
        print(f'=> passed value for {dir} is a {type(dir)}')
        print(f'=> passed value for {rep} is a {type(rep)}')
        print(f'=> passed value for {repw} is a {type(repw)}')

def main():
    base_dir = r' '
    replace = ''
    replace_with = ' '
    rename_file(dir=base_dir, rep=replace, repw=replace_with)

if __name__ == '__main__':
    main()


