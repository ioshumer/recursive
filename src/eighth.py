import os


def list_files_of_dir(dir_path):
    files_list = []
    _processor(dir_path, files_list)
    return files_list


def _processor(parent_dir, files_list: list, element_name=None):
    current_path = os.path.join(parent_dir, element_name) if element_name is not None else parent_dir
    if os.path.isfile(current_path):
        files_list.append(current_path)
        return
    else:
        elements_list = os.listdir(current_path)
        for element in elements_list:
            _processor(current_path, files_list, element)
