# Author: Nam Nguyen Hoai
import mainframe
import wx


class MyApplication(wx.App):

    def OnInit(self):
        self.frame = mainframe.MainFrame(None, title='This app is to monitor')
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True
