import tkinter as tk 
frame = tk.Tk() 
frame.title('GFG Cursors') 
frame.geometry('200x200') 
frame.config(cursor="dot blue") 
tk.Label(frame, text="Text cursor", 
         cursor="xterm #0000FF").pack() 
  
tk.Button(frame, text="Circle cursor", 
          cursor="circle #FF00FF").pack() 
  
tk.Button(frame, text="Plus cursor", 
          cursor="plus red").pack() 
a = tk.Button(frame, text='Exit') 
a.config(cursor="dot green red") 
a.pack() 
  
frame.mainloop() 