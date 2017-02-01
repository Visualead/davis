import os
import re


def rename_and_start_from_0(input_dir, ext='png', verbose=True):
    """
    Renames files to start from 00000.png

    input /users/sagirorlich/test/final_frame001.png
    output /users/sagirorlich/test/00000.png
    """
    num = 0
    for path in os.listdir(input_dir):
        if os.path.splitext(path)[1] != ('.' + ext):
            continue
        full_path = os.path.join(input_dir, path)
        base_name = os.path.basename(path)
        extension = os.path.splitext(path)[1]
        numbers = re.findall(r'\d+', base_name)
        if len(numbers) == 0:
            print('error - no number found in file {}'.format(path))
        if len(numbers) > 1:
            print('error - more then one number found in file {}'.format(path))
        number = num
        new_base_name = str(number).zfill(5) + '.jpg'
        new_full_path = full_path.replace(base_name, new_base_name)
        if verbose:
            print('Renaming \n{}\nto\n{}'.format(full_path, new_full_path))
        os.rename(full_path, new_full_path)
        num += 1


def rename_gygo_db(input_path, ext='.png', verbose=True):
    for dir in os.listdir(input_path):
        dir_path = os.path.join(input_path, dir)
        if verbose:
            print('Running folder: ' + dir_path)
        for subdir in os.listdir(dir_path):
            if subdir[0] == '.':
                continue  # invisible folder/file
            rename_and_start_from_0(os.path.join(dir_path, subdir))


if __name__ == '__main__':
    db_path = '/Users/eddie/Documents/Projects/Repositories/davis/data/DAVIS/Results/Segmentations/variable/vl'
    rename_gygo_db(db_path, ext='.png')


