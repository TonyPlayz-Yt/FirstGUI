import tkinter as tk


# https://stackoverflow.com/questions/20044559/how-to-pip-or-easy-install-tkinter-on-windows#20044745
# see https://github.com/TonyPlayz-Yt/FirstGUI.git

top = tk.Tk()
mb= tk.Menubutton (text="condiments", relief=tk.RAISED )
mb.grid()
mb.menu =  tk.Menu ( mb, tearoff = 0 )
mb["menu"] =  mb.menu

mayoVar = tk.IntVar()
ketchVar = tk.IntVar()

mb.menu.add_checkbutton ( label="mayo",
                          variable=mayoVar )
mb.menu.add_checkbutton ( label="ketchup",
                          variable=ketchVar )

mb.pack()
top.mainloop()
# root.mainloop()