from color_utils import *

_verbose = False


def stripped_raw_input(prompt):
    if _verbose:
        print("stripped_raw_input ( prompt: {} )".format(prompt))
    input_val = raw_input(get_green(prompt))
    input_val = input_val.strip()
    return input_val

