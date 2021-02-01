import os, json
from error import error_logger
import requests

def url_is_secure(data):
    """
    => Check if the passed in url is a secure
    url
    => based on whether the url starts with https or https://
    """
    return data.startswith("https://")

class PackageManager():
    def __init__(self, search_for_packages):
        self.packages = self.get_all_packages(search_for_packages)

        PackageManager.install_packages(self.packages)

    def get_all_packages(self, package_dir):
        """
        Get the list of packages to install as an array
        """
        if package_dir == ".":
            return self.read_all_packages(
                os.path.join(
                    os.getcwd(),
                    f"{os.path.basename(os.getcwd())}.json"
                )
            )
        else:
            return [package_dir]

    def read_all_packages(self, filename):
        """
        Read all the required packages from
        the config file
        and return it

        if config file not present , throws out
        an error
        and returns an empty array of 
        packages
        """
        if os.path.exists(filename) and os.path.isfile(filename):
            with open(filename, "r") as reader:
                return json.load(reader)["packages"]
        else:
            error_logger("Config file does not exists")
            return []

    @staticmethod
    def install_packages(packages):
        """
        Get all the packages
        """
        installed_packages = []
        module_path = os.path.join(os.getcwd(), "mod")

        # create the module directory 
        # if the directory does'nt exist
        if not os.path.exists(module_path):
            os.mkdir(module_path)

        for index, package in enumerate(packages):
            if url_is_secure(package):
                # if the url is secure
                print(f"INSTALLING:installing {package}")
                try:
                    """
                    => Try reading the raw file
                    => get the basepath of the url(filename) 
                    => removes the (.) in the basepath and created
                    a folder for putting the file 
                    => open the file and write the string form 
                    of the extracted raw data
                    =>else if an exception occurs throw out an error
                    """
                    data = requests.get(package)
                    project_path = os.path.basename(package)
                    dir_path = project_path.split(".")[0]
                    
                    if dir_path in os.listdir(module_path):
                        pass
                    else:
                        os.mkdir(os.path.join(module_path, dir_path))
                        file_path = os.path.join(module_path, dir_path, project_path)

                        with open(file_path, "w") as writer:
                            writer.write(str(data.raw))

                    installed_packages.append(package)
                except Exception as e:
                    error_logger("Failed to install")
                print(f"INSTALLED:{installed_packages}")
            else:
                error_logger("Packages should be hosted on a secure connection")









