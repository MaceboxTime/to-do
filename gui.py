import tkinter as tk
from tkinter import messagebox
from task_manager import add_task, delete_task, mark_complete, update_task, load_tasks


def update_list():
    task_list.delete(0, tk.END)
    tasks = load_tasks()
    for i, task in enumerate(tasks, start=1):
        task_list.insert(tk.END, f"{i}. {task[0]} - {task[1]} (Due: {task[2]}) [{task[3]}]")


def add_task_gui():
    title = title_entry.get()
    description = desc_entry.get()
    due_date = due_date_entry.get()
    if title and due_date:
        add_task(title, description, due_date)
        update_list()
        title_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Title and Due Date are required!")


def delete_task_gui():
    selected = task_list.curselection()
    if selected:
        delete_task(selected[0])
        update_list()
    else:
        messagebox.showerror("Error", "Please select a task to delete!")


def mark_complete_gui():
    selected = task_list.curselection()
    if selected:
        mark_complete(selected[0])
        update_list()
    else:
        messagebox.showerror("Error", "Please select a task to mark as complete!")


def update_task_gui():
    selected = task_list.curselection()
    if selected:
        index = selected[0]
        tasks = load_tasks()
        title_entry.delete(0, tk.END)
        desc_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
        title_entry.insert(0, tasks[index][0])
        desc_entry.insert(0, tasks[index][1])
        due_date_entry.insert(0, tasks[index][2])

        def save_update():
            update_task(index, title_entry.get(), desc_entry.get(), due_date_entry.get())
            update_list()
            update_window.destroy()

        update_window = tk.Toplevel(root)
        update_window.title("Update Task")
        tk.Label(update_window, text="Title:").pack()
        tk.Entry(update_window, textvariable=tk.StringVar(value=tasks[index][0])).pack()
        tk.Label(update_window, text="Description:").pack()
        tk.Entry(update_window, textvariable=tk.StringVar(value=tasks[index][1])).pack()
        tk.Label(update_window, text="Due Date:").pack()
        tk.Entry(update_window, textvariable=tk.StringVar(value=tasks[index][2])).pack()
        tk.Button(update_window, text="Save", command=save_update).pack()
    else:
        messagebox.showerror("Error", "Please select a task to update!")


root = tk.Tk()
root.title("To-Do List Manager")

frame = tk.Frame(root)
frame.pack(pady=10)

title_label = tk.Label(frame, text="Title:")
title_label.grid(row=0, column=0)
title_entry = tk.Entry(frame)
title_entry.grid(row=0, column=1)

desc_label = tk.Label(frame, text="Description:")
desc_label.grid(row=1, column=0)
desc_entry = tk.Entry(frame)
desc_entry.grid(row=1, column=1)

due_date_label = tk.Label(frame, text="Due Date:")
due_date_label.grid(row=2, column=0)
due_date_entry = tk.Entry(frame)
due_date_entry.grid(row=2, column=1)

add_button = tk.Button(frame, text="Add Task", command=add_task_gui)
add_button.grid(row=3, column=0, columnspan=2, pady=5)

task_list = tk.Listbox(root, width=50)
task_list.pack(pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task_gui)
delete_button.pack()

complete_button = tk.Button(root, text="Mark Complete", command=mark_complete_gui)
complete_button.pack()

update_button = tk.Button(root, text="Update Task", command=update_task_gui)
update_button.pack()

update_list()

root.mainloop()