import os, platform
from clint.textui import colored as color

class OperatingSystem():
    @staticmethod
    def os_name():
        return platform.system()

    @staticmethod
    def user_name():
        return platform.uname().node

    @staticmethod
    def path():
        return os.getcwd()

def list_directories(directory):
    dir_list = os.listdir(directory)
    for index, p in enumerate(dir_list):
        path = os.path.join(directory, p)
        if os.path.isfile(path):
            print(color.green(str(p)))
        else:
            print(color.blue(str(p)))
            
