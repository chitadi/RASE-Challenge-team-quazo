
import os
import importlib
import sys
current_directory =  os.path.dirname(__file__)
# python_file_name = os.path.splitext(os.path.basename(__file__))[0]
# sys.path.append(current_directory)

files_or_folder = os.listdir(current_directory)
# print()
python_files = [_file for _file in files_or_folder if os.path.splitext(_file)[-1] == ".py" and _file != "__init__.py"]
for py_file in python_files:
    get_file_name = lambda path: os.path.splitext(os.path.basename(path))[0]
    file_name = get_file_name(py_file)

    try:
        module = importlib.import_module("." + file_name, package="models")
        globals()[file_name] = getattr(module, file_name)
    except AttributeError:
        print(f"Module '{file_name}' with object {file_name} not found")


    # print(py_file)
    
