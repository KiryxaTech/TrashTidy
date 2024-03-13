from TrashTidy.recycle_bin import *
from TrashTidy.tray import *
from TrashTidy.window import *

class Main:
    def __init__(self) -> None:
        tray = Tray()
        tray.run_to_new_thread()
        
if __name__ == '__main__':
    Main()