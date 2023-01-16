import os


class FilePathUtil:
    def __init__(self):
        return

    def get_file_name(self, file_path):
        file_name = os.path.basename(file_path)
        return file_name
