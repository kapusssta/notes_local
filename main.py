import tkinter as tk

root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', True)
root.attributes('-alpha', 0.9)
root.geometry("400x300")
root.configure(bg='#2c2c2c')


def add_task():
    text = entry.get().strip()
    if text:
        print(f'Добавлена новая задача: {text}')
        entry.delete(0, tk.END)
    else:
        print("Введите задачу")

def start_move(event):
    global offset_x, offset_y
    offset_x = event.x
    offset_y = event.y

def do_move(event):
    new_x = event.x_root - offset_x
    new_y = event.y_root - offset_y
    root.geometry(f'+{new_x}+{new_y}')


title_bar = tk.Label(
    root,
    text="☰  План дел",
    bg='#3a3a3a',
    fg='white',
    font=("Arial", 10, "bold"),
    )

title_bar.pack(fill=tk.X, padx=5, pady=(5, 2))
root.bind('<Button-1>', start_move)
root.bind('<B1-Motion>', do_move)


close_btn = tk.Button(
    root,
    text="  X  ",
    command=root.quit,
    bg='red',
    fg='white',
    relief='flat'
)
close_btn.place(x=370, y=5)

input_frame = tk.Frame(root, bg='#2c2c2c')
input_frame.pack(padx=10, pady=10)

entry = tk.Entry(
    input_frame,
    width=25,
    bg='#444',
    fg='white',
    insertbackground='pink'
)
entry.pack(side=tk.LEFT, padx=(0, 5))
entry.bind('<Return>', lambda event: add_task())

add_btn = tk.Button(
    root,
    text="  +  ",
    command=add_task,
    bg='green',
    fg='white',
    relief='flat'
)
add_btn.place(x=0, y=5)


root.mainloop()

