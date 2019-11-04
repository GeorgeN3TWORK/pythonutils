import re
from .utils import *

_verbose = False
regex = re.compile("[^a-zA-Z]")
fail_log = "You must input y (for yes) or n (for no)!"


def _strip_non_letters(target):
    if _verbose:
        print("_strip_non_letters ( target: {} )".format(target))

    return regex.sub("", target)


def _yes_or_no_validation(target):
    if _verbose:
        print("yes_or_no_validation ( target: {} )".format(target))

    target = _strip_non_letters(target)
    target = target.lower()

    if len(target) <= 0:
        print(fail_log)
        return False

    if target[0] == "y":
        return True

    if target[0] == "n":
        return True

    print(fail_log)
    return False


def yes_or_no(prompt):
    if _verbose:
        print("yes_or_no ( prompt: {} )".format(prompt))

    input_yes_or_no = stripped_raw_input("{} {}/{}: ".format(prompt, get_yellow("y"), get_yellow("n")))

    while not _yes_or_no_validation(input_yes_or_no):
        input_yes_or_no = stripped_raw_input("{}/{}: ".format(get_yellow("y"), get_yellow("n")))

    input_yes_or_no = _strip_non_letters(input_yes_or_no)

    if input_yes_or_no[0] == 'y':
        return True

    if input_yes_or_no[0] == 'n':
        return False

    print("Not sure how you reached this point. Your input was: {}".format(input_yes_or_no))
    return False
