import ctypes
import os

import winshell


def open() -> None:
    os.startfile(winshell.recycle_bin())


def empty() -> None:
    ctypes.windll.shell32.SHEmptyRecycleBinA(None, None, 1)

def get_size() -> int:
    pass
