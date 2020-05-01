import os
import sys


def resource_path(relative_path):
    try:
        base_path = os.path.join(sys._MEIPASS, './resource/')
    except AttributeError:
        base_path = os.path.abspath('./resource/')
    return os.path.join(base_path, relative_path)
