import os
import sys
import glob

path_dir = ["E:\\"]
# file_name = "extraction"
extensions = [".mkv", ".mp4"]

dir = {"time": ["E:\\"], "data": ["D:\\"]}

# this class is only searching for files in E:\
class search_f:
    def __init__(self, file_name, path_name):
        value = dir.__contains__(path_name)
        if not value:
            return "not found"
        self.path_name = path_name
        paths = dir[path_name]
        self.paths = paths
        self.file_name = file_name

    def find_file(self):
        for base_path in self.paths:
            files = os.listdir(base_path)
            for file in files:
                if self.file_name in file.lower():
                    path = os.path.join(base_path, file)
                    os.startfile(path)
                    return "found"
        return "not found"

    def find_file_glob(self):
        for base_path in self.paths:
            for ext in extensions:
                glob_path = base_path + "**\\*" + ext
                file_iterator = glob.iglob(glob_path, recursive=True)

                value_to_return = "not found"
                while True:
                    pth_of_file = next(file_iterator)
                    # print(pth_of_file)
                    if self.file_name in pth_of_file.lower():
                        os.startfile(pth_of_file)
                        value_to_return = "found"
                        break
                    else:
                        value_to_return = "not found"
                return value_to_return


# s = search_f(file_name)
# r = s.find_file_glob()
# print(r)
