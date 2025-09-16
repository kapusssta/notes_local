import tkinter as tk

tasks = []

root = tk.Tk()
root.overrideredirect(True)
root.attributes('-topmost', True)
root.attributes('-alpha', 0.9)
root.geometry("400x300")
root.configure(bg='#2c2c2c')

def update_check_llist():
    for widget in check_list.winfo_children():
        widget.destroy()

    for i, task in enumerate(tasks):
        task_text = task["text"]
        is_completed = task["completed"]

        task_row = tk.Frame(check_list, bg="#2c2c2c")
        task_row.pack(fill=tk.X, pady=2)

        cb_var = tk.BooleanVar(value=is_completed)
        cb = tk.Checkbutton(
            task_row,
            text=task_text,
            variable=cb_var,
            bg="#2c2c2c",
            fg='white' if not is_completed else '#888',
            selectcolor='#2c2c2c',
            activebackground='#2c2c2c'
        )
        cb.pack(side=tk.LEFT)

        del_btn = tk.Button(
            task_row,
            text="🗑️",
            bg='#555',
            fg='white',
            relief='flat',
        )
        del_btn.pack(side=tk.RIGHT)


def add_task():
    text = entry.get().strip()
    if text:
        tasks.append({"text": text, "completed": False})
        print(f'Добавлена новая задача: {text}')
        entry.delete(0, tk.END)
        update_check_llist()
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



def toggle_task(index, var):
    tasks[index]["completed"] = var.get()
    update_check_llist()

def delete_task(index):
    del tasks[index]
    update_check_llist()

check_list = tk.Frame(root, bg="#2c2c2c")
check_list.place(x=10, y=80, width=380, height=200)

title_bar = tk.Label(
    root,
    text="☰  План дел",
    bg='#3a3a3a',
    fg='white',
    font=("Arial", 10, "bold"),
    )
title_bar.place(x=0, y=0, width=400, height=30)


title_bar.bind('<Button-1>', start_move)
title_bar.bind('<B1-Motion>', do_move)


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
input_frame.place(x=10, y=40, width=380, height=30)
entry = tk.Entry(
    input_frame,
    width=25,
    bg='#444',
    fg='white',
    insertbackground='pink'
)
entry.pack(side=tk.LEFT, padx=(0, 5), fill=tk.BOTH, expand=True)

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

