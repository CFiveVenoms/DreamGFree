import wx
import tkinter
from tkinter import *
def wxGUI():
    app = wx.PySimpleApp()
    win = wx.Frame(None,title ='Simple Editor',size =(410,335))
    bkg = wx.Panel(win)
    loadButton = wx.Button(bkg,label='Open')
    saveButton = wx.Button(bkg,label='Save')
    filename = wx.TextCtrl(bkg)
    contents = wx.TextCtrl(bkg,style=wx.TE_MULTILINE | wx.HSCROLL)

    hbox = wx.BoxSizer()
    hbox.Add(filename,proportion = 1,flag = wx.EXPAND)
    hbox.Add(loadButton,proportion = 0,flag = wx.LEFT,border = 5)
    hbox.Add(saveButton,proportion = 0,flag = wx.LEFT,border = 5)

    vbox = wx.BoxSizer()
    vbox.Add(hbox,proportion = 0,flag = wx.EXPAND | wx.ALL,border = 5)
    vbox.Add(contents,proportion = 1,flag = wx.EXPAND | wx.ALL | wx.BOTTOM | wx.RIGHT,border = 5)

    bkg.SetSizer(vbox)
    win.Show()
    app.MainLoop()
def TkinterGUI():
    top = tkinter.Tk()
    label =tkinter.Button(top,text = 'Hello World!',command = top.quit())
    label.pack()
    tkinter.mainloop()