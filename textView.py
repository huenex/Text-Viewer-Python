# -*- coding: cp1252 -*-
import wx
import subprocess
import os
import io
import time
                   
class windowClass(wx.Frame):
    def __init__ (self, *args, **kwargs):
        super(windowClass, self).__init__(*args, **kwargs)

        self.basicGUI()
       
    def basicGUI(self):
        self.Center()
        global panel, gamePath1, gamePath2, gamePath3, gamePath4, windowDetect, MySnapshot
        panel = wx.Panel(self, size=(400,400))
        menuBar = wx.MenuBar()
        menuFile = wx.Menu()
        
        self.SetTitle("text thing")
        
        from string import ascii_uppercase
        my_data = open("textFile.txt")
                       
        textObj = wx.TextCtrl(panel, style=wx.TE_MULTILINE, size=(350,350))
        textObj.SetLabel(str(my_data.read()))

        launchTitle1 = wx.Button(panel, id=wx.ID_ANY, label="Start",pos=(0, 0))

        def launch1 (event):
            print "hello"
                
        launchTitle1.Bind(wx.EVT_BUTTON, launch1)

        def closewindow(event):
            self.Close()

        exitItem = menuFile.Append(wx.ID_EXIT, 'Exit', 'Close the App')
        
        menuBar.Append(menuFile, 'File')
        
        self.SetMenuBar(menuBar)
        
        self.Bind(wx.EVT_MENU, self.Quit, exitItem)

        self.Show(True)

    def Quit(self, e):
        self.Close()   
def main():

    app = wx.App()
    windowClass(None, style = wx.CAPTION | wx.MINIMIZE_BOX , size=((400, 400)))
    app.MainLoop()

main()
        
