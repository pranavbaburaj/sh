import os, json
from error import error_logger
import requests

def url_is_secure(data):
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

        if not os.path.exists(module_path):
            os.mkdir(module_path)

        for index, package in enumerate(packages):
            if url_is_secure(package):
                print(f"INSTALLING:installing {package}")
                try:
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









