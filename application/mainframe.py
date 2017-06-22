# Author: Nam Nguyen Hoai
# coding: utf-8
import os
import wx


class MainFrame(wx.Frame):
    def __init__(self, parent, id=wx.ID_ANY, title='Nam Nguyen Hoai',
                 pos=wx.DefaultPosition, size=(600, 400),
                 style=wx.DEFAULT_FRAME_STYLE, name="Main Frame"):
            super(MainFrame, self).__init__(parent, id, title, pos, size,
                                            style, name)
            self.panel = wx.Panel(self)
            # Setup Icon
            path = os.path.abspath('./images/monitor_icon.png')
            icon = wx.Icon(path, wx.BITMAP_TYPE_PNG)
            self.SetIcon(icon)
            # Setup Menus and MenuBar
            filemenu1 = wx.Menu()
            fileitems1 = filemenu1.Append(wx.ID_EDIT, 'Thoát',
                                          'Thoát chương trình')
            menubar = wx.MenuBar()
            menubar.Append(filemenu1, '&File')
            self.SetMenuBar(menubar)
            self.Bind(wx.EVT_MENU, self.on_quit, fileitems1)
            # Create squares to input name and password
            self.user_name = wx.TextCtrl(self)
            self.password = wx.TextCtrl(self, style=wx.TE_PASSWORD)
            # Layout
            sizer = wx.FlexGridSizer(2, 2, 10, 10)
            sizer.Add(wx.StaticText(self, label='Tên máy của bạn:'),
                      0, wx.ALIGN_CENTER_VERTICAL)
            sizer.Add(self.user_name, 0, wx.EXPAND)
            sizer.Add(wx.StaticText(self, label='Mật khẩu dịch vụ:'),
                      0, wx.ALIGN_CENTER_VERTICAL)
            sizer.Add(self.password, 0, wx.EXPAND)
            msizer = wx.BoxSizer(wx.VERTICAL)
            msizer.Add(sizer, 1, wx.EXPAND | wx.ALL, 20)
            btnszr = wx.StdDialogButtonSizer()
            button = wx.Button(self, wx.ID_OK)
            button.SetDefault()
            btnszr.AddButton(button)
            msizer.Add(btnszr, 0, wx.ALIGN_CENTER | wx.ALL, 12)
            btnszr.Realize()
            self.SetSizer(msizer)

    def on_quit(self, mess):
        self.Close()

    def GetUsername(self):
        return self.username.GetValue()

    def GetPassword(self):
        return self.password.GetValue()