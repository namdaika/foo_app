# Author: Nam Nguyen Hoai

import mainframe
import wx


class MyApplication(wx.App):

    def OnInit(self):
        self.frame = mainframe.MainFrame(None, title='This app to monitor')
        self.SetTopWindow(self.frame)
        self.frame.Show()


def main():
    app = MyApplication()
    app.MainLoop()


if __name__ == '__main__':
    main()
