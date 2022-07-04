import tkinter as tk
import tkinter.ttk as ttk
from ttkthemes import ThemedStyle
from tkinter import filedialog

def darkmode(window):
    
    #   Setting the theme
    #style = ttk.Style(window)
    #window.tk.call('source', "themes/black/black.tcl")
    #style.theme_use('black')
##    style = ThemedStyle(window)
##    style.set_theme("alt")
##    style.configure("Accentbutton", fg='white')
##    style.configure("Togglebutton", fg='white')

    return style

def main_window():
    
    window = tk.Tk()
    window.title("YT Playlist installer")
    window.resizable(False, False)

##
##    style= darkmode(window)
    
    #   Pretty useless as its all incorrect but keeping it for possible convienince in the future
    window.rowconfigure(0, minsize=1, weight=1)
    window.rowconfigure(1, minsize=1, weight=1)
    window.rowconfigure(2, minsize=200, weight=1)
    window.columnconfigure(0, minsize=0, weight=1)
    window.columnconfigure(1, minsize=0, weight=1)
    window.columnconfigure(2, minsize=0, weight=0)
    
    txt_edit = tk.Text(window)
    T_txt_edit = tk.Text(window)

    #   Text on buttons and prerequisite syntax 
    frm_buttons = tk.Frame(window)
    T_frm_buttons = ttk.Frame(window)
    btn_gen= tk.Button(frm_buttons, text="Generate")
    T_btn_gen= ttk.Button(T_frm_buttons, text="Generate")
    btn_change= tk.Button(frm_buttons, text="Change Directory")
    T_btn_change= ttk.Button(T_frm_buttons, text="Change Directory")

    #   Dark/Lihjt Switch
    #   mode can be dark/light

    mode = ('dark')
    btn_switch= tk.Button(text=mode)
##    T_btn_switch= ttk.Button(text=mode)

    btn_switch.place(x=612, y=423)
##    T_btn_switch.place(x=612, y=423)

    ##btn_switch.(mode = ('light'))
    ##T_btn_switch.get

    #   Text is blue and width is based on the allignment in lines 33,34
    link_entry = tk.Entry(fg="blue", width=89)
    T_link_entry = ttk.Entry(width=89)
    link_entry2 = tk.Entry(fg="blue", width=89)
    T_link_entry2 = ttk.Entry(width=89)

    #   Buttons placed onto a grid within a grid, giving the nice symmetrycal allignment
    frm_buttons.grid(row=0, column=0, sticky="w")
    btn_gen.grid(row=0, column=0, sticky="ne", padx=5, pady=4)
    btn_change.grid(row=1, column=0, sticky="s", padx=5)

    #   Entry spaces in opposite directions, ineffecient but idc
    link_entry.grid(row=0, column=0, sticky="ne", padx=5, pady=8)
    link_entry2.grid(row=0, column=0, sticky="se", padx=5, pady=4)

    #   The large textfield, also im tired of writing these so have fun deciphering the rest :)
    txt_edit.grid(row=2, column=0, sticky="nesw", padx=5, pady=5)

def change_theme(windows,theme):

    windows.mainf.configure(background= '{}'.format(color))


    window.update()
    
    window.mainloop()
    
main_window()

