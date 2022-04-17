import tkinter as tk


win = tk.Tk()
win.title('계산기')



tk.Button(win, text='1', width=10, height=5).grid(column=0, row=1)
tk.Button(win, text='2', width=10, height=5).grid(column=1, row=1)
tk.Button(win, text='3', width=10, height=5).grid(column=2, row=1)
tk.Button(win, text='4', width=10, height=5).grid(column=3, row=1)

tk.Button(win, text='5', width=10, height=5).grid(column=0, row=2)
tk.Button(win, text='6', width=10, height=5).grid(column=1, row=2)
tk.Button(win, text='7', width=10, height=5).grid(column=2, row=2)
tk.Button(win, text='8', width=10, height=5).grid(column=3, row=2)

tk.Button(win, text='9', width=10, height=5).grid(column=0, row=3)
tk.Button(win, text='0', width=10, height=5).grid(column=1, row=3)
tk.Button(win, text='+', width=10, height=5).grid(column=2, row=3)
tk.Button(win, text='-', width=10, height=5).grid(column=3, row=3)

tk.Button(win, text='/', width=10, height=5).grid(column=0, row=4)
tk.Button(win, text='*', width=10, height=5).grid(column=1, row=4)
tk.Button(win, text='C', width=10, height=5).grid(column=2, row=4)
tk.Button(win, text='=', width=10, height=5).grid(column=3, row=4)



win.mainloop()