from threading import Thread
from pathlib import Path

from pystray import Icon, Menu, MenuItem as Item
from PIL import Image

# Function to open an image file and return a PIL Image object
def get_pil_image(fp: str|Path) -> Image.open:
    return Image.open(fp)

class Tray(Icon):
    def __init__(self) -> None:
        # Define the menu with a single 'Quit' item
        menu = Menu(
            Item('Quit', self.quit)
        )
        
        # Initialize the Icon with the name, title, icon, and menu
        super().__init__(
            name='TrashTidy',
            title='TrashTidy   |   0B   |   0%',
            icon=get_pil_image(Path(r'icons\dark\0.png')),
            menu=menu
        )
        
    # Method to set the icon
    def set_icon(self, fp: str|Path) -> None:
        self.icon = get_pil_image(fp)
        
    # Method to set the title
    def set_title(self, conv_size: str, percent_size: int|str) -> None:
        self.title = f'TrashTidy   |   {conv_size}   |   {percent_size}%'
    
    # Method to run the application in a new thread
    def run_to_new_thread(self):
        Thread(target=self.run).start()
    
    # Method to stop the application
    def quit(self):
        self.stop()