import tkinter as tk
from tkinter import filedialog
from pytube import Playlist
from pytube import YouTube

window = tk.Tk()
window.title("YT Playlist installer")
window.resizable(False, False)
window.geometry("655x457")

#p= "https://www.youtube.com/playlist?list=PLDD2Be2ZfSPjCInDBSAID2zYE4gKBFZ1Y"
p=('')

GL_var= tk.StringVar()
CD_var= tk.StringVar()

links=[]

jinx=0
tinks=0

BADD=('White')
BADL=('Black')


def gui(window):

    def PressedD():

        global jinx
        jinx=0
        SubmitDark()
        

    def ClearL():

        links.clear()
        Lightmode()
        
    def ClearD():

        global jinx
        links.clear()
        jinx=1
        Darkmode()
        
        

    def ClearDark():

        F = ('white')
        TXT = ('#24292e')

        i=1
        
        ListBox = tk.Listbox(window,fg=F,bg=TXT,width=107, height=24)

        if links != []:
            for item in range(len(links)):
                ListBox.insert(i, links[item])
                i=i+1
            
        ListBox.grid(row=1, column=0, sticky="nesw", padx=4, pady=5)
        
        command=Darkmode()
        
    def SubmitLight():
        
        global tinks
        global BADD
        global BADL
        global F
        
        F = ("Black")
        TXT = ("White")
        
        i=1
        
        ListBox = tk.Listbox(window,fg=F,bg=TXT,width=107, height=24)

        p = Playlist(GL_var.get())

        print (GL_var.get())
        str = GL_var.get()
        print (str)


        if links==[] or len(links)==0 or len(links)==1:
            if(str.startswith('youtube.com')or('https://youtube.com')or('https://www.youtube.com')):
                links.clear()
                for url in p.video_urls:
                    
                    ListBox.insert(i, f' 'f'{i}'f': 'f'{url}')
                    links.append(f' 'f'{i}'f': 'f'{url}')
                    i=i+1
            
                    BADL=('Black')
                    BADD=('White')
                    tinks=1
                    
        if len(links) <= 2 :
            print('yep')
            links.clear()
            ListBox.insert(1, f'ERROR: link is incorrect')
            links.append(f'ERROR: link is incorrect')
            print ('nothing here')
            BADD = ('red')
            BADL = ('red')


        print ('oh someonethuibguabaj:' and links[0])
        ListBox.grid(row=1, column=0, sticky="nesw", padx=4, pady=5)
        command=Lightmode()        
        
    def SubmitDark():

        global BADD
        global BADL
        global jinx

        F = ('white')
        TXT = ('#24292e')
        
        i=1

        ListBox = tk.Listbox(window,fg=F,bg=TXT,width=107, height=24)


        p = Playlist(GL_var.get())

        print (GL_var.get())
        str = GL_var.get()
        print (str)
        
        if links==[] or len(links)==0 or len(links)==1:
            if(str.startswith('youtube.com')or('https://youtube.com')or('https://www.youtube.com')):
                links.clear()
                for url in p.video_urls:
                    
                    ListBox.insert(i, f' 'f'{i}'f': 'f'{url}')
                    links.append(f' 'f'{i}'f': 'f'{url}')
                    i=i+1
            
                    BADL=('Black')
                    BADD=('White')
                    tinks=1
                    
        if len(links) <= 2 :
            print('yep')
            links.clear()
            ListBox.insert(1, f'ERROR: link is incorrect')
            links.append(f'ERROR: link is incorrect')
            print ('nothing here')
            BADD = ('red')
            BADL = ('red')

                
        ListBox.grid(row=1, column=0, sticky="nesw", padx=4, pady=5)
        command=Darkmode()
    
    def Lightmode():
        
        global GL_var
        global CD_var
        global p
        global BADL

        F = ("Black")
        TXT = ("White")

        i=1
        ListBox = tk.Listbox(window,fg=F,bg=TXT,width=107, height=24)
        
        for item in range(len(links)):
            ListBox.insert(i, links[item])
            ListBox.itemconfig(item)
            print(item, links[item])
            i=i+1
            
        print (len(links))    
        
        window['background']= '#f0f0f0'
        
        mode = ('dark')
        btn_switch= tk.Button(text=mode,command=ClearDark)
        btn_switch.place(x=612, y=423)

        mode = ('clear')
        btn_switch2= tk.Button(text=mode,command=ClearL)
        btn_switch2.place(x=610, y=395)
        
        frm_buttons = tk.Frame(window)
        btn_gen= tk.Button(frm_buttons, text="Generate", command=SubmitLight)
        btn_change= tk.Button(frm_buttons, text="Change Directory")

        link_entry = tk.Entry(fg=BADL, textvariable=GL_var, width=89)
        
        p=(GL_var.get())
        
        link_entry2 = tk.Entry(fg="blue", textvariable=CD_var, width=89)

        frm_buttons.grid(row=0, column= 0, sticky="w")
        btn_gen.grid(row=0, column=0, sticky="ne", padx=5, pady=4)
        btn_change.grid(row=1, column=0, sticky="s", padx=5)

        link_entry.grid(row=0, column=0, sticky="ne", padx=5, pady=8)
        link_entry2.grid(row=0, column=0, sticky="se", padx=5, pady=4)

        ListBox.grid(row=1, column=0, sticky="nesw", padx=4, pady=5)


    def Darkmode():

        
        global GL_var
        global CD_var
        global p
        global BADD

        F = ('white')
        B = ('#2f363d')
        TXT = ('#24292e')

        i=1
        ListBox = tk.Listbox(window,fg=F,bg=TXT,width=107, height=24)

        window.configure(bg = B)    

        for item in range(len(links)):
            ListBox.insert(i, links[item])
            ListBox.itemconfig(item)
            print(item, links[item])
            i=i+1
            
        mode = ('light')
        btn_switch= tk.Button(fg=F,bg=B,text=mode,command=Lightmode)
        btn_switch.place(x=611, y=423)

        mode = ('clear')
        btn_switch2= tk.Button(fg=F,bg=B,text=mode,command=ClearD)
        btn_switch2.place(x=610, y=395)
        
         
        frm_buttons = tk.Frame(window, bg=B)
        btn_gen= tk.Button(frm_buttons, text="Generate",fg=F,bg=B,command=PressedD)
        btn_change= tk.Button(frm_buttons, text="Change Directory",fg=F,bg=B)

        link_entry = tk.Entry(window, textvariable=GL_var, fg=BADD , bg=TXT, width=89)
        
        p=(GL_var.get())
        
        link_entry2 = tk.Entry(window, textvariable=CD_var, fg="white", bg=TXT, width=89)

        frm_buttons.grid(row=0, column=0, sticky="w")
        btn_gen.grid(row=0, column=0, sticky="ne", padx=5, pady=4)
        btn_change.grid(row=1, column=0, sticky="s", padx=5)

        link_entry.grid(row=0, column=0, sticky="ne", padx=5, pady=8)
        link_entry2.grid(row=0, column=0, sticky="se", padx=5, pady=4)

        ListBox.grid(row=1, column=0, sticky="nesw", padx=4, pady=5)
        
    def Printsmth():

        label = tk.Label(window,text= "OOGA FUCKING BOOGA")
        label.place(x=10,y=12)
              
    ClearDark()
        
        
    window.update()
    
    window.mainloop()
    
gui(window)

