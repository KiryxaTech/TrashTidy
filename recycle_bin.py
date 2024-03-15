import ctypes
import os

import winshell
import win32com.client

MAX_BIN_SIZE_MB = 26411

def open() -> None:
    os.startfile(winshell.recycle_bin())


def empty() -> None:
    ctypes.windll.shell32.SHEmptyRecycleBinA(None, None, 1)


def get_size() -> int:
    shell = win32com.client.Dispatch("Shell.Application")
    recycle_bin = shell.NameSpace(10)  # 10 corresponds to the Recycle Bin
    items = recycle_bin.Items()
    
    total_size = 0
    for item in items:
        total_size += item.Size

    return total_size
