import os


def list_files_of_dir(dir_path):
    files_list = _processor(dir_path)
    return files_list


def _processor(parent_dir, element_name=None):
    current_path = os.path.join(parent_dir, element_name) if element_name is not None else parent_dir
    if os.path.isfile(current_path):
        return current_path
    else:
        elements_list = os.listdir(current_path)
        files_list = []
        for element in elements_list:
            result = _processor(current_path, element)
            if isinstance(result, list):
                files_list.extend(result)
            else:
                files_list.append(result)
        return files_list
