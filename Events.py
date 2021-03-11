#!/usr/bin/env python3
'''
Tkinter skeleton app
'''
import tkinter as tk
import random

class Application(tk.Frame):
    '''Sample tkinter application class'''

    def __init__(self, master=None, title="<application>", **kwargs):
        '''Create root window with frame, tune weight and resize'''
        super().__init__(master, **kwargs)
        self.master.title(title)
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)
        self.grid(sticky="NEWS")
        self.createWidgets()

    def createWidgets(self):
        '''Create all the widgets'''
        self.S = tk.StringVar()
        self.E = tk.Entry(self, textvariable = self.S)
        self.E.grid(column=0, row=0, sticky="WE")
        #self.L = tk.Label(self, textvariable = self.S)
        self.L = tk.Label(self, textvariable = self.S, takefocus=True, highlightthickness=1)
        self.L.grid(column=1, row=0, sticky="WE")
        self.B = tk.Button(self, text = "Quit", command = self.master.quit)
        self.B.grid(column=1, row=1)
        #self.master.event_add('<<Check>>', '<Motion>', '<Any-Key>', '<FocusIn>')
        Event = '<Any-Key>'
        for obj in self.master, self, self.E, self.B, self.L:
            def f(*a, s=obj): print(s, a)
            obj.bind(Event, f)

app = Application(title="Sample application")
app.mainloop()
