import tkinter as tk
import tkinter.ttk as ttk
from tkinter import filedialog

class Win(tk.Frame):

    def __init__(window, master):
        tk.Frame.__init__(window, master)
        window.master = master

        txt_edit = tk.Text(window.mainf)
        txt_edit.grid(window.mainf, row=2, column=0, sticky="nesw", padx=5, pady=5)

        window.mainf = tk.Frame(master)
        window.mainf.grid(row=0, column=0, sticky="w")
        
        btn_gen= tk.Button(window.mainf, text="Generate")
        btn_change= tk.Button(window.mainf, text="Change Directory")
        
        btn_gen.grid(window.mainf, row=0, column=0, sticky="ne", padx=5, pady=4)
        btn_change.grid(window.mainf, row=1, column=0, sticky="s", padx=5)
        
        window.theme_btn()
        window.themes = ['dark','light']


        link_entry = tk.Entry(window.mainf, fg="blue", width=89)
        link_entry2 = tk.Entry(window.mainf, fg="blue", width=89)





    def theme_btn(window):

        window.dark = tk.Button(window.mainf, text="light",
                                command=lambda: window.change_Theme(
                                    window.Themes[light]))
        window.light = tk.Button(window.mainf, text="dark",
                                command=lambda: window.change_Theme(
                                    window.Themes[dark]))    
        
        btn_switch.place(x=612, y=423)

    def change_theme(windows,theme):

        windows.mainf.configure(background= '{}'.format(theme))
    

root = tk.Tk()
root.title("YT Playlist installer")
root.resizable(False, False)
root.update()
        
app = Win(root)
    
root.mainloop()
    

