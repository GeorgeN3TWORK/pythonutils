import os

_verbose = False


def notify(title, text):
    if _verbose:
        print("workbook_search ( title: {} , text: {} )".format(title, text))

    os.system("""
              osascript -e 'display notification "{}" with title "{}"'
              """.format(text, title))
