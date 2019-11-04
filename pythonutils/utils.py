from color_utils import *
from hidden_utils import is_hidden
import os

_verbose = False


def stripped_raw_input(prompt):
    if _verbose:
        print("stripped_raw_input ( prompt: {} )".format(prompt))
    input_val = raw_input(get_green(prompt))
    input_val = input_val.strip()
    return input_val


def get_file_paths(path, recursive=False, ending_with=""):
    debug = "get_file_paths ( at_path: {} , recursive: {} , endingWith: {} )".format(path, recursive, ending_with)
    if _verbose:
        print(debug)

    file_paths = []

    if os.path.isdir(path) is False:
        print(debug + " | Your entered path is not a directory!")
    else:
        file_names = [obj for obj in os.listdir(path)]
        # file_names = [obj for obj in os.listdir(at_path)] \
        #     if ending_with is "" else [obj for obj in os.listdir(at_path) if obj.endswith(ending_with)]

        if _verbose:
            print("file_names: {}".format(len(file_names)))

        for file_name in file_names:
            if not is_hidden(file_name):
                file_path = "{}/{}".format(path, file_name)
                file_path = file_path.replace("//", "/")
                isdir = os.path.isdir(file_path)

                if _verbose:
                    print("file_name: {} | file_path: {} | isdir: {}".format(file_name, file_path, isdir))

                if isdir:
                    if recursive:
                        file_paths.extend(get_file_paths(file_path, recursive))
                else:
                    add_entry = True

                    if ending_with is not "":
                        add_entry = file_path.endswith(ending_with)

                    if add_entry:
                        file_paths.append(file_path)

    return file_paths


def get_file_name_from_path(path, with_extension=False):
    if _verbose:
        print "extract_file_name_from_path ( path: {} , with_extension: {} )".format(path, with_extension)

    return os.path.basename(path) if with_extension else os.path.splitext(os.path.basename(path))[0]


def get_parent_dir(target_path, amount=1):
    debug = "get_parent_dir ( target_file: {} , amount: {} )".format(target_path, amount)
    if _verbose:
        print debug

    if amount < 0:
        print "{} | amount can't be less than zero, setting it to 1".format(debug)
        amount = 1

    parent_dir = "Not found"

    i = 0
    while i < amount:
        i += 1
        target_path = os.path.join(target_path, os.pardir)
        parent_dir = os.path.abspath(target_path)

    return parent_dir
