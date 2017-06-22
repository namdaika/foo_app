# Author: Nam Nguyen Hoai
# coding: utf-8
import wx

import mainframe


class MyApplication(wx.App):

    def OnInit(self):
        self.frame = mainframe.MainFrame(None, title="Ứng dụng monitor "
                                                     "card đồ họa")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True
