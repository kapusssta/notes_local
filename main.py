import tkinter as tk

root = tk.Tk()

root.overrideredirect(True)

root.attributes('-topmost', True)

root.attributes('-alpha', 0.9)

root.geometry("400x300")

root.configure(bg='#2c2c2c')

close_btn = tk.Button(
    root,
    text="  X  ",
    command=root.quit,
    bg='red',
    fg='white',
    relief='flat'
)
close_btn.place(x=370, y=5)

root.mainloop()