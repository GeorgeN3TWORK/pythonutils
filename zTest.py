from pythonutils.os_utils import *
from pythonutils.utils import *


def test_ensure_dir_path_exists():
    example_file = "/Users/georgekatsaros/Desktop/NestedExample/NestedExample/example.txt"
    ensure_dir_path_exists(example_file)


def test_get_file_paths():
    # print ""
    # script_path = os.path.realpath(__file__)
    # script_dir = os.path.dirname(script_path)
    # script_dir_paths = get_file_paths(script_dir, recursive=False, ending_with="")
    script_dir_paths = get_file_paths("/Users/georgekatsaros/Projects/Legendary/Config/Excel", recursive=False, ending_with=".xlsx")
    for script_dir_path in script_dir_paths:
        print script_dir_path


def test_colors():
    print("Hi there this is {} and it's nice".format(get_black("_black")))
    print("Hi there this is {} and it's nice".format(get_red("_red")))
    print("Hi there this is {} and it's nice".format(get_yellow("_yellow")))
    print("Hi there this is {} and it's nice".format(get_blue("_blue")))
    print("Hi there this is {} and it's nice".format(get_magenta("_magenta")))
    print("Hi there this is {} and it's nice".format(get_cyan("_cyan")))
    print("Hi there this is {} and it's nice".format(get_white("_white")))
    print("Hi there this is {} and it's nice".format(get_bright_black("_bright_black")))
    print("Hi there this is {} and it's nice".format(get_bright_red("_bright_red")))
    print("Hi there this is {} and it's nice".format(get_bright_green("_bright_green")))
    print("Hi there this is {} and it's nice".format(get_bright_yellow("_bright_yellow")))
    print("Hi there this is {} and it's nice".format(get_bright_black("_black")))
    print("Hi there this is {} and it's nice".format(get_bright_blue("_bright_blue")))
    print("Hi there this is {} and it's nice".format(get_bright_magenta("_bright_magenta")))
    print("Hi there this is {} and it's nice".format(get_bright_cyan("_bright_cyan")))
    print("Hi there this is {} and it's nice".format(get_bright_white("_bright_white")))


test_ensure_dir_path_exists()
# test_get_file_paths()
# test_colors()

