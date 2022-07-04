import tkinter as tk
from tkinter import filedialog
from pytube import Playlist


window = tk.Tk()
window.title("YT Playlist installer")
window.resizable(False, False)
window.geometry("655x457")

p= "https://www.youtube.com/playlist?list=PLDD2Be2ZfSPjCInDBSAID2zYE4gKBFZ1Y"

GL_var= tk.StringVar()
CD_var= tk.StringVar()

links=[]


def gui(window):
    

    def ClearDark():
        
        F = ('white')
        TXT = ('#24292e')

        i=1
        
        ListBox = tk.Listbox(window,fg=F,bg=TXT,width=107, height=24)
        for item in range(len(links)):
            ListBox.insert(i, links[item])
            ListBox.itemconfig(item)
            #print(item, links[item])
            i=i+1
        ListBox.grid(row=1, column=0, sticky="nesw", padx=4, pady=5)
        
        command=Darkmode()
        
    def SubmitLight():
        
        F = ("Black")
        TXT = ("White")
        i=1
        
        ListBox = tk.Listbox(window,fg=F,bg=TXT,width=107, height=24)
        PL = Playlist(p)

        if links==[]:
            for url in PL.video_urls:

                ListBox.insert(i, f' 'f'{i}'f': 'f'{url}')
                LKS=ListBox.get(i)
                links.append(f' 'f'{i}'f': 'f'{url}')
                #print(ListBox.get(i))
                i=i+1
            

        ListBox.grid(row=1, column=0, sticky="nesw", padx=4, pady=5)
        command=Lightmode()        
        
    def SubmitDark():

        F = ('white')
        TXT = ('#24292e')
        
        i=1

        ListBox = tk.Listbox(window,fg=F,bg=TXT,width=107, height=24)
        PL = Playlist(p)
        print(i)
        if links==[]:
            for url in PL.video_urls:
                
                ListBox.insert(i, f' 'f'{i}'f': 'f'{url}')
                LKS=ListBox.get(i)
                links.append(f' 'f'{i}'f': 'f'{url}')
                #print(ListBox.get(i))
                i=i+1
                
        ListBox.grid(row=1, column=0, sticky="nesw", padx=4, pady=5)
        truth=1
        command=Darkmode()
    
    def Lightmode():

        F = ("Black")
        TXT = ("White")

        i=1
        ListBox = tk.Listbox(window,fg=F,bg=TXT,width=107, height=24)

        print (links)
        
        for item in range(len(links)):
            ListBox.insert(i, links[item])
            ListBox.itemconfig(item)
            print(item, links[item])
            i=i+1
            
        
        window['background']= '#f0f0f0'
        
        mode = ('dark')
        btn_switch= tk.Button(text=mode,command=ClearDark)
        btn_switch.place(x=612, y=423)

        frm_buttons = tk.Frame(window)
        btn_gen= tk.Button(frm_buttons, text="Generate", command=SubmitLight)
        btn_change= tk.Button(frm_buttons, text="Change Directory")

        link_entry = tk.Entry(fg="blue", width=89)
        link_entry2 = tk.Entry(fg="blue", width=89)

        frm_buttons.grid(row=0, column= 0, sticky="w")
        btn_gen.grid(row=0, column=0, sticky="ne", padx=5, pady=4)
        btn_change.grid(row=1, column=0, sticky="s", padx=5)

        link_entry.grid(row=0, column=0, sticky="ne", padx=5, pady=8)
        link_entry2.grid(row=0, column=0, sticky="se", padx=5, pady=4)

        ListBox.grid(row=1, column=0, sticky="nesw", padx=4, pady=5)


    def Darkmode():

        F = ('white')
        B = ('#2f363d')
        TXT = ('#24292e')

        window.configure(bg = B)
        
        mode = ('light')
        btn_switch= tk.Button(fg=F,bg=B,text=mode,command=Lightmode)
        btn_switch.place(x=612, y=423)
         
        frm_buttons = tk.Frame(window, bg=B)
        btn_gen= tk.Button(frm_buttons, text="Generate",fg=F,bg=B,command=SubmitDark)
        btn_change= tk.Button(frm_buttons, text="Change Directory",fg=F,bg=B)

        link_entry = tk.Entry(window, textvariable=GL_var, fg="white", bg=TXT, width=89)
        p=GL_var
        print (GL_var.get())
        link_entry2 = tk.Entry(window, textvariable=CD_var, fg="white", bg=TXT, width=89)

        frm_buttons.grid(row=0, column=0, sticky="w")
        btn_gen.grid(row=0, column=0, sticky="ne", padx=5, pady=4)
        btn_change.grid(row=1, column=0, sticky="s", padx=5)

        link_entry.grid(row=0, column=0, sticky="ne", padx=5, pady=8)
        link_entry2.grid(row=0, column=0, sticky="se", padx=5, pady=4)
        
    def Printsmth():

        label = tk.Label(window,text= "OOGA FUCKING BOOGA")
        label.place(x=10,y=10)

              
    ClearDark()
    Darkmode()
        
        
    window.update()
    
    window.mainloop()
    
gui(window)

