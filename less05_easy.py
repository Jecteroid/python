#codding utf-8
import os
import shutil
import sys

# Введите make, если хотите удалить
# Введите remove, если хотите удалить
# Введите mydirs, если хотите посмотреть папки в текущий директории
# Введите copyfile, если хотите создать копию файла, из которого запущен данный скрипт

def make_dir(name):

    if os.path.isdir(name):
        print(f'Папку {name} не удалось создать')

    else:
        os.mkdir(name)
        print(f'Папка {name} создана')


def remove_dir(name):

    if os.path.isdir(name):
        os.rmdir(name)
        print(f'Папка {name} удалена')

    else:
        print(f'Папка {name} не найдена')


def my_dirs():
    print('Ваши папки:')
    for dir_or_file in os.listdir(os.getcwd()):
        if os.path.isdir(dir_or_file):
            print(dir_or_file)


def copy_file(file):
    new_file_name, new_file_ex = file.split('.')
    new_file_name += '-copy'
    new_file_name = '.'.join([new_file_name, new_file_ex])

    shutil.copy(file, new_file_name)

def main():
    # Задача-1:
    # Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
    # из которой запущен данный скрипт.
    # И второй скрипт, удаляющий эти папки.

    if 'make' in sys.argv:
        for i in range(1, 10):
            make_dir(f'dir{i}')

    if 'remove' in sys.argv:
        for i in range(1, 10):
            remove_dir(f'dir_{i}')

    # Задача-2:
    # Напишите скрипт, отображающий папки текущей директории.

    if 'mydirs' in sys.argv:
        my_dirs()

    # Задача-3:
    # Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

    if 'copyfile' in sys.argv:
        copy_file(__file__)

if __name__ == '__main__':
    main()