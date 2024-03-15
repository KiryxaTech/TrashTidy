from threading import Thread
from pathlib import Path

from recycle_bin import *
from tray import *
from window import *
from recycle_bin import *


def get_convert_size(size):
    units = ["B", "KB", "MB", "GB", "TB"]
    for unit in units:
        if size < 1024:
            return f'{round(size, 2)}{unit}'
        size /= 1024
        
def get_percent_size(max_size=MAX_BIN_SIZE_MB):
    return round(get_size() / 1024**2 / max_size, 2)
    

class Main:
    def __init__(self) -> None:
        self.tray = Tray()
        self.tray.run_to_new_thread()
        
        window = Window()
        window.after(1000, self.bin_update)
        
        window.mainloop()
        
    def bin_update(self):
        fill_level = self.bin_fill_level(get_size() / 1024**2)
        
        self.tray.set_icon(Path(f'icons\\dark\\{fill_level}.png'))
        self.tray.set_title(get_convert_size(get_size()), get_percent_size())
        
    def bin_fill_level(self, size_bytes):
        if size_bytes <= 0:
            return 0
        elif size_bytes < MAX_BIN_SIZE_MB * 1/4:
            return 1
        elif size_bytes < MAX_BIN_SIZE_MB * 2/4:
            return 2
        elif size_bytes < MAX_BIN_SIZE_MB * 3/4:
            return 3
        else:
            return 4
        
if __name__ == '__main__':
    Main()