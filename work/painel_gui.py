"""Painel With Tkinter"""

from tkinter import *
from tkinter import ttk


class PainelWindow:
    """Render Elements"""
    def __init__(self) -> None:
        """Render Elements"""

        self.root = Tk()
        self.root.title("Painel")
        self.root.geometry("500x400")


        self.painel = PanedWindow(
            orient=VERTICAL,
            # bd=4, 
            relief='raised', 
            bg='#353b50')

        self.painel.pack(
            fill=BOTH, 
            expand=1)


        self.top = PanedWindow(
            self.painel, 
            orient=VERTICAL, 
            relief='raised', 
            bd=4, 
            bg='#1e3543')

        self.painel.add(self.top)

        self.container_1 = PanedWindow(
            self.painel, 
            orient=VERTICAL, 
            relief='raised', 
            bd=4, 
            bg='#1e3543')

        self.painel.add(self.container_1)

        self.container_1


        # top_ = Label(self.top, text="ola senhores")
        # self.top.add(top_)



        self.root.mainloop()

    def content(self, arg) -> None:
        pass


if __name__ == '__main__':
    PainelWindow()


