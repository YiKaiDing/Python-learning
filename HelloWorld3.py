# Import wx module.
#
# Define an object of Application class .
#
#
# Create a top level window as object of wx.Frame class. Caption and size parameters are given in constructor.
#
#
# Although other controls can be added in Frame object, their layout cannot be managed.Hence, put a Panel object into the Frame.
#
# Add a StaticText object to display ‘Hello World’ at a desired position inside the window.

# Activate the frame window by show() method.

#Enter the main event loop of Application object.

import wx

app = wx.App()
window = wx.Frame(None, title="wxPython Frame", size=(300, 200))
panel = wx.Panel(window)
label = wx.StaticText(panel, label="Hello World", pos=(100, 50))
window.Show(True)
app.MainLoop()