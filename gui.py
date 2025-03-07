#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.24.1
#  in conjunction with Tcl version 8.6
#    Jul 30, 2019 08:57:31 PM PKT  platform: Windows NT

import sys
import webbrowser
import sqlite3
from os import chdir
from time import sleep

chdir('webpages/')

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

class Toplevel1:

    #-------------------------------------------------------------------------#
    def open_webpage(self):
        webpage=self.variable.get()
        ind=self.files.index(webpage)
        webbrowser.open_new_tab(str(self.keys[ind])+'.html')            
        return

    def get_results(self):
        conn = sqlite3.connect('0database.db')
        cur = conn.cursor()
        
        search=self.Entry1.get()
        if len(search)>1:
            search='%'+search+'%'
            cur.execute("SELECT ID, NAME FROM NAMES_DOC WHERE NAME LIKE ?",(search,))
        elif len(search):
            search=search+'%'
            cur.execute("SELECT ID, NAME FROM NAMES_DOC WHERE NAME LIKE ?",(search,))
        else:
            cur.execute("SELECT ID, NAME FROM NAMES_DOC")   
        rows = cur.fetchall()
        self.files=[]
        self.keys=[]
        for i in rows:
            self.keys.append(i[0])
            self.files.append(i[1])
        conn.close()

        if len(self.keys)==0:
            self.files.append('No match found')
                
        self.variable.set(self.files[0])
        self.Combobox1.destroy()
        self.create_option_menu()
        return

    def create_option_menu(self):
        self.Combobox1 = ttk.Combobox(self.Frame1, textvariable=self.variable, values=self.files)
        self.Combobox1.place(relx=0.023, rely=0.6, relheight=0.192
                , relwidth=0.686)
        self.Combobox1.configure(background="white")
        self.Combobox1.configure(foreground="black")

        if len(self.keys)==0:
            self.Combobox1.configure(state="disabled")
            self.Button1.configure(state="disabled")
        else:
            self.Combobox1.configure(state="readonly")
            self.Button1.configure(state="active")
        return

    
    def verifying(self,type):
        self.label1=tk.Label(self.Frame1,text='Verifying ' + type + '...')
        self.label1.place(relx=0.1, rely=0.1, relheight=0.192
                , relwidth=0.8)
        self.label1.configure(activebackground="#ececec")
        self.label1.configure(activeforeground="#000000")
        self.label1.configure(background="#d9d9d9")
        self.label1.configure(foreground="#000000")
        self.label1.configure(highlightbackground="#d9d9d9")
        self.label1.configure(highlightcolor="black")
        self.progress=ttk.Progressbar(orient='horizontal',length=100,mode='determinate')
        self.progress.place(relx=0.1, rely=0.4, relheight=0.192
                , relwidth=0.8)
        conn = sqlite3.connect('0database.db')
        cur = conn.cursor()
        cur.execute("SELECT ID FROM NAMES_DOC")
        rows = cur.fetchall()
        i=1
        self.progress['maximum']=10828
        for row in rows:
            self.progress['value']=i
            self.progress.update()
            if i==row[0]:
                i+=1
                continue
            else:
                i+=2
        self.label1.destroy()
        self.progress.destroy()
        conn.close()
    #------------------------------------------------------------------------#
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("450x150+377+161")
        top.title("Hashmites of Kakori")
        top.iconbitmap('../icon.ico')
        top.configure(background="#d9d9d9")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.022, rely=0.067, relheight=0.833
                , relwidth=0.956)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(width=430)
        
        self.verifying(type='files')
        self.verifying(type='database')

        self.Entry1 = tk.Entry(self.Frame1)
        self.Entry1.place(relx=0.023, rely=0.2,relheight=0.192, relwidth=0.686)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")

        self.Button1 = tk.Button(self.Frame1)
        self.Button1.place(relx=0.744, rely=0.6, relheight=0.192, relwidth=0.23)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Open''')
        self.Button1.configure(command=self.open_webpage)

        self.Button2 = tk.Button(self.Frame1)
        self.Button2.place(relx=0.744, rely=0.2, relheight=0.192, relwidth=0.23)
        self.Button2.configure(activebackground="#ececec")
        self.Button2.configure(activeforeground="#000000")
        self.Button2.configure(background="#d9d9d9")
        self.Button2.configure(disabledforeground="#a3a3a3")
        self.Button2.configure(foreground="#000000")
        self.Button2.configure(highlightbackground="#d9d9d9")
        self.Button2.configure(highlightcolor="black")
        self.Button2.configure(pady="0")
        self.Button2.configure(text='''Search''')
        self.Button2.configure(command=self.get_results)        
        #-------------------------------------------------------------------#        
        self.variable=tk.StringVar()        
        conn = sqlite3.connect('0database.db')
        cur = conn.cursor()
        cur.execute("SELECT ID, NAME FROM NAMES_DOC")   
        rows = cur.fetchall()
        self.keys=[]
        self.files=[]
        for i in rows:
            self.keys.append(i[0])
            self.files.append(i[1])
        conn.close()
        self.variable.set(self.files[0])
        #-------------------------------------------------------------------#
        
        self.create_option_menu()

if __name__ == '__main__':
    vp_start_gui()





