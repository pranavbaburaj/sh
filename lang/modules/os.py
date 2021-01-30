import os, platform

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