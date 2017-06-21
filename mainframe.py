# Author: Nam Nguyen Hoai

import wx


class MainFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title='Nam Nguyen Hoai',
                 pos=wx.DefaultPosition, size=(600, 400),
                 style=wx.DEFAULT_FRAME_STYLE, name="Main Frame"):
            super(MainFrame, self).__init__(parent, id, title, pos, size,
                                            style, name)
            self.panel = wx.Panel(self)
