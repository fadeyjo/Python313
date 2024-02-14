import os
import time

SIZE_OF_KILOBYTE = 1024
ROOT_FOR_SCANNING = 'test'


def creating_info(path):
    return time.strftime('%d.%m.%Y at %H:%M:%S', time.localtime(os.path.getctime(path)))


for selected_directory, directories_in_selected_directory, files_in_selected_directory in os.walk(ROOT_FOR_SCANNING):
    for directory in directories_in_selected_directory:
        print(f'{directory} - dir - create time: {creating_info(os.path.join(selected_directory, directory))}.')
    for file in files_in_selected_directory:
        size_of_file = os.path.getsize(os.path.join(selected_directory, file))
        print(f'{file} - file - {size_of_file} bytes ({size_of_file / SIZE_OF_KILOBYTE} kilobytes) - create time: {creating_info(os.path.join(selected_directory, file))}.')
