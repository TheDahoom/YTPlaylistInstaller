import tkinter as tk
import sys
from tkinter import filedialog
from pytube import Playlist


window = tk.Tk()
window.title("YT Playlist installer")
window.resizable(False, False)

def gui(window):
    
    def Lightmode():
        
        txt_edit = tk.Text(window)
        
        window['background']= '#f0f0f0'
        
        mode = ('dark')
        btn_switch= tk.Button(text=mode,command=Darkmode)
        btn_switch.place(x=612, y=423)

        #   Text on buttons and prerequisite syntax 
        frm_buttons = tk.Frame(window)
        btn_gen= tk.Button(frm_buttons, text="Generate")
        btn_change= tk.Button(frm_buttons, text="Change Directory")

        #   Text is blue and width is based on the allignment in lines 33,34
        link_entry = tk.Entry(fg="blue", width=89)
        link_entry2 = tk.Entry(fg="blue", width=89)

        #   Buttons placed onto a grid within a grid, giving the nice symmetrycal allignment
        frm_buttons.grid(row=0, column=0, sticky="w")
        btn_gen.grid(row=0, column=0, sticky="ne", padx=5, pady=4)
        btn_change.grid(row=1, column=0, sticky="s", padx=5)

        #   Entry spaces in opposite directions, ineffecient but idc
        link_entry.grid(row=0, column=0, sticky="ne", padx=5, pady=8)
        link_entry2.grid(row=0, column=0, sticky="se", padx=5, pady=4)

        #   The large textfield, also im tired of writing these so have fun deciphering the rest :)
        txt_edit.grid(row=2, column=0, sticky="nesw", padx=5, pady=5)


    def Darkmode():

        F = ('white')
        B = ('#2f363d')
        TXT = ('#24292e')
        
        txt_edit = tk.Text(window,fg=F,bg=TXT)

        window.configure(bg = B)
        
        mode = ('light')
        btn_switch= tk.Button(fg=F,bg=B,text=mode,command=Lightmode)
        btn_switch.place(x=612, y=423)

        #   Text on buttons and prerequisite syntax 
        frm_buttons = tk.Frame(window, bg=B)
        btn_gen= tk.Button(frm_buttons, text="Generate",fg=F,bg=B,command=Printsmth)
        btn_change= tk.Button(frm_buttons, text="Change Directory",fg=F,bg=B)

        #   Text is blue and width is based on previous allignments
        link_label = tk.Label(window, text="OOGA FICLOMGA BPOOFA")
        link_entry = tk.Entry(fg="white", bg=TXT, width=89, link_label,sticky="w")
        link_entry2 = tk.Entry(fg="white", bg=TXT, width=89)

        #   Buttons placed onto a grid within a grid, giving the nice symmetrycal allignment
        frm_buttons.grid(row=0, column=0, sticky="w")
        btn_gen.grid(row=0, column=0, sticky="ne", padx=5, pady=4)
        btn_change.grid(row=1, column=0, sticky="s", padx=5)

        #   Entry spaces in opposite directions, ineffecient but idc
        link_entry.grid(row=0, column=0, sticky="ne", padx=5, pady=8)
        link_entry2.grid(row=0, column=0, sticky="se", padx=5, pady=4)

        #   The large textfield, also im tired of writing these so have fun deciphering the rest :)
        txt_edit.grid(row=2, column=0, sticky="nesw", padx=5, pady=5)

        link_entry = command=Printsmth

    def Printsmth():

        label = tk.Label(window,text= "OOGA FUCKING BOOGA")
        label.place(x=10,y=10)
        
        

        
    Darkmode()
        
        
    window.update()
    
    window.mainloop()
    
gui(window)

