from pathlib import Path

import customtkinter as ctk
from customtkinter import CTkFrame, CTkLabel, CTkButton
from PIL import Image


def create_ctkimage(fp: str|Path):
    """ Create ad return ctk.CTkImage

    Args:
        fp (str|Path): file path

    Returns:
        CTkImage: image for CTkButton
    """
    return ctk.CTkImage(Image.open(Path(fp)))


class Page(CTkFrame):
    """
    Page class represents a single page in the application.
    """
    _pages = []
    
    def __init__(self, master, page_name: str):
        super().__init__(master=master, width=550, height=300, corner_radius=0)
        
        # Title of the page
        self.title = CTkLabel(
            master=self,
            width=0,
            height=40,
            font=('Segoe UI Bold', 25),
            text=page_name
        )
        self.title.place(x=10, y=5)
        
        # Added self (Page object) to _pages
        Page.add_page(self)
        
    @classmethod
    def get_pages(cls):
        """ Adds a new page to the list of pages

        Returns:
            list: return Page._pages (cls._pages)
        """
        return cls._pages
    
    @classmethod
    def add_page(cls, page):
        """
        Adds a new page to the list of pages.
        """
        if not isinstance(page, Page):
            raise ValueError("The page must be an instance of Page class.")
        cls._pages.append(page)


class NavigationButton(CTkButton):
    """
    NavigationButton class represents a button in the navigation menu.
    """
    _buttons = []
    stack_count = 0
    
    def __init__(self, master, linked_page: Page, image: ctk.CTkImage):
        self.linked_page = linked_page
        
        super().__init__(master=master,
                         width=40,
                         height=40,
                         fg_color='transparent',
                         hover_color='#323232',
                         image=image,
                         text='',
                         command=self.command)
        
        NavigationButton.add_button(self)
        
    def command(self):
        self.place_linked_page()
        self.set_button_color()
    
    def place_linked_page(self):
        for page in Page.get_pages():
            page.place_forget()
        
        self.linked_page.place(x=50, y=0)
        
    def set_button_color(self):
        for btn in NavigationButton.get_buttons():
            btn.configure(fg_color='transparent')
        self.configure(fg_color='#323232')
        
        
    @classmethod
    def get_buttons(cls):
        """ Adds a new button to the list of pages

        Returns:
            list: return NavigationButton._buttons (cls._buttons)
        """
        return cls._buttons
    
    @classmethod
    def add_button(cls, button):
        """
        Adds a new button to the list of buttons.
        """
        if not isinstance(button, NavigationButton):
            raise ValueError("The page must be an instance of Page class.")
        cls._buttons.append(button)


class NavigationMenu(CTkFrame):
    """
    NavigationMenu class represents the navigation menu of the application.
    """
    def __init__(self, master):
        super().__init__(master=master, width=50, height=300,
                         fg_color='#242424', corner_radius=0)
    
    def stack_button(self, button: NavigationButton):
        """Method to place the button in the navigation menu.

        Args:
            button (NavigationButton): button
        """
        # Делаем начальный отступ в 5 пкс
        # Умножаем сумму размера иконки и отступа между кнопками
        # Складываем начальный отступ и получившееся значение
        y = 5 + (40 + 5) * NavigationButton.stack_count
        x = 5
        button.place(x=x, y=y)
        
        NavigationButton.stack_count += 1


class Window(ctk.CTk):
    """
    Window class represents the main application window.
    """
    def __init__(self):
        super().__init__()
        
        self.title('TrashTidy ➡️ Settings')
        self.geometry('600x300')
        self.resizable(0, 0)
        
        # Initialize settings frame and navigation menu
        self.navigation_menu = NavigationMenu(self)
        
        # Settings objects
        self.settings_frame = Page(self, page_name='Bin settings')
        self.settings_image = create_ctkimage(r'icons\recycle-bin.png')
        self.settings_button = NavigationButton(master=self,
                                                linked_page=self.settings_frame,
                                                image=self.settings_image)
        
        self.settings_button.place_linked_page()
        
        # Themes objects
        self.themes_frame = Page(self, page_name='Themes')
        self.themes_image = create_ctkimage(r'icons\paint-roller.png')
        self.themes_button = NavigationButton(master=self,
                                              linked_page=self.themes_frame,
                                              image=self.themes_image)
        
        # Stack navigation buttons in the navigation menu
        self.navigation_menu.stack_button(self.settings_button)
        self.navigation_menu.stack_button(self.themes_button)
        
        # Place settings frame and navigation menu in the window
        self.navigation_menu.place(x=0, y=0)
        
        # Start the application
        self.mainloop()

            
Window()