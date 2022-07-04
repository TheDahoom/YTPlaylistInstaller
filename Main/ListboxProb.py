import tkinter as tk
import sys
from tkinter import filedialog
from pytube import Playlist



window = tk.Tk()
window.title("YT Playlist installer")
window.resizable(False, False)
window.geometry("655x457")

p= "https://www.youtube.com/playlist?list=PLDD2Be2ZfSPjCInDBSAID2zYE4gKBFZ1Y"

GL_var= tk.StringVar()
CD_var= tk.StringVar()

Truth=0

def gui(window):

    def Submit():

        print(GL_var.get())
        print (p)
        PL = Playlist(p)
        print (PL)
        Truth = 1
        command=Darkmode()
    
    def Lightmode():

        F = ("Black")
        TXT = ("White")
        
        ListBox = tk.Listbox(window,fg=F,bg=TXT,width=107, height=24)
        
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
        frm_buttons.grid(row=0, column= 0, sticky="w")
        btn_gen.grid(row=0, column=0, sticky="ne", padx=5, pady=4)
        btn_change.grid(row=1, column=0, sticky="s", padx=5)

        #   Entry spaces in opposite directions, ineffecient but idc
        link_entry.grid(row=0, column=0, sticky="ne", padx=5, pady=8)
        link_entry2.grid(row=0, column=0, sticky="se", padx=5, pady=4)

        #   The large textfield, also im tired of writing these so have fun deciphering the rest :)
        ListBox.grid(row=1, column=0, sticky="nesw", padx=4, pady=5)


    def Darkmode():

        F = ('white')
        B = ('#2f363d')
        TXT = ('#24292e')

        window.configure(bg = B)

        ListBox = tk.Listbox(window, fg=F, bg=TXT, width=107, height=24)
        ListBox.insert(1, 'bam')
        
        mode = ('light')
        btn_switch= tk.Button(fg=F,bg=B,text=mode,command=Lightmode)
        btn_switch.place(x=612, y=423)
        
        #   Text on buttons and prerequisite syntax 
        frm_buttons = tk.Frame(window, bg=B)
        btn_gen= tk.Button(frm_buttons, text="Generate",fg=F,bg=B,command=Submit)
        btn_change= tk.Button(frm_buttons, text="Change Directory",fg=F,bg=B)

        ListBox.insert(2, 'bom')
        
        #print (GL_var)
        #   Text is blue and width is based on previous allignments
        link_entry = tk.Entry(window, textvariable=GL_var, fg="white", bg=TXT, width=89)
        p=GL_var
        print (GL_var.get())
        link_entry2 = tk.Entry(window, textvariable=CD_var, fg="white", bg=TXT, width=89)

        #   Buttons placed onto a grid within a grid, giving the nice symmetrycal allignment
        frm_buttons.grid(row=0, column=0, sticky="w")
        btn_gen.grid(row=0, column=0, sticky="ne", padx=5, pady=4)
        btn_change.grid(row=1, column=0, sticky="s", padx=5)

        #   Entry spaces in opposite directions, ineffecient but idc
        link_entry.grid(row=0, column=0, sticky="ne", padx=5, pady=8)
        link_entry2.grid(row=0, column=0, sticky="se", padx=5, pady=4)
        
        ListBox.insert(3, 'badwwm')
        
        if Truth == 1:
            
            ListBox = tk.Listbox(window, fg=F, bg=TXT, width=107, height=24)
            ListBox.insert(6, 'bad321wwm')
            i = 1
            for url in PL.video_urls:  
                #ListBox.insert(i)
                ListBox.insert(i, f' 'f'{i}'f': 'f'{url}')
                #ListBox.insert(i, f'{url.title}')
                i=i+1
        ListBox.insert(4, 'ba32131')
        
        #   The large textfield, also im tired of writing these so have fun deciphering the rest :)
        ListBox.grid(row=1, column=0, sticky="nesw", padx=4, pady=5)

        ListBox.insert(5, 'badw3213wm')


##        #   The large textfield, also im tired of writing these so have fun deciphering the rest :)
##        ListBox.grid(row=1, column=0, sticky="nesw", padx=4, pady=5)
##      

    def Printsmth():

        label = tk.Label(window,text= "OOGA FUCKING BOOGA")
        label.place(x=10,y=10)
        
        

        
    Darkmode()
        
        
    window.update()
    
    window.mainloop()
    
gui(window)

