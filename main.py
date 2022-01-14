#Import - Libs

import os
from tkinter import *

#Import - Packages

from Utils.assets import *
from Utils.defs import *

#Tkinter

window = Tk()

width = 620
height = 370
width_screen = window.winfo_screenwidth()
height_screen = window.winfo_screenheight()
pos_x = int(width_screen / 2 - width / 2)
pos_y = int(height_screen / 2 - height / 2)

directory = os.path.dirname(__file__)
assets = assets(directory)
roots = roots(window)

window.geometry(f'{width}x{height}+{pos_x}+{pos_y}')
window.resizable(False,False)
window['background'] = '#000'

build(window, directory, roots, assets)
click_show(window, directory, roots, 'menu')

window.mainloop()
