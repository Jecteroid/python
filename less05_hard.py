#codding utf-8
# Задание-1:
# Доработайте реализацию программы из примера examples/5_with_args.py,
# добавив реализацию следующих команд (переданных в качестве аргументов):
#   cp <file_name> - создает копию указанного файла
#   rm <file_name> - удаляет указанный файл (запросить подтверждение операции)
#   cd <full_path or relative_path> - меняет текущую директорию на указанную
#   ls - отображение полного пути текущей директории
# путь считать абсолютным (full_path) -
# в Linux начинается с /, в Windows с имени диска,
# все остальные пути считать относительными.

# Важно! Все операции должны выполняться в той директории, в который вы находитесь.
# Исходной директорией считать ту, в которой был запущен скрипт.

# P.S. По возможности, сделайте кросс-платформенную реализацию.

import os
import sys
import shutil


def print_help():
    print("help - получение справки")
    print("mkdir <dir_name> - создание директории")
    print("ping - тестовый ключ")
    print("cp <file_name> - создает копию указанного файла")
    print("rm <file_name> - удаляет указанный файл (запросить подтверждение операции)")
    print("cd <full_path or relative_path> - меняет текущую директорию на указанную")
    print("ls - отображение полного пути текущей директории")


def make_dir():
    if not name:
        print("Необходимо указать имя директории вторым параметром")
        return
    dir_path = os.path.join(os.getcwd(), dir_name)
    try:
        os.mkdir(dir_path)
        print('директория {} создана'.format(dir_name))
    except FileExistsError:
        print('директория {} уже существует'.format(dir_name))


def copy_file():
    if not name:
        print("Необходимо указать имя файла вторым параметром")
        return

    if os.path.isfile(name):
        new_file_name, new_file_ex = name.split('.')
        new_file_name += '-copy'
        new_file_name = '.'.join([new_file_name, new_file_ex])

        shutil.copy(name, new_file_name)
        print(f'Копия файла {name} создана')

    else:
        print(f'Файла {name} не существует')

def remove_file():
    if not name:
        print("Необходимо указать имя файла вторым параметром")
        return

    if os.path.isfile(name):
        ans = input('Вы уверены, что хотите безвозвратно удалить этот файл?(Y/N)')
        if ans == 'y' or ans == 'Y':
            os.remove(name)
            print(f'Файл {name} удалён')

        else:
            print(f'Файл {name} не будет удалён')

    else:
        print(f'Файл {name} не найден')

def change_dir():
    if not name:
        print("Необходимо указать имя директории вторым параметром")
        return

    if os.path.isdir(name):
        os.chdir(name)
        print(f'Успешно перешел в директорию {name}')

    else:
        print(f'Не удалось перейти в директорию {name}')

def dir_cwd():
    print(os.getcwd())

def ping():
    print("pong")

do = {
    "help": print_help,
    "mkdir": make_dir,
    "ping": ping,
    "cp": copy_file,
    "rm": remove_file,
    "cd": change_dir,
    "ls": dir_cwd
}

try:
    name = sys.argv[2]
except IndexError:
    name = None

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()

    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")
