import os
import json
import tkinter as tk
from tkinter import messagebox

def load_tasks():
    if os.path.exists("tasks.json"):
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
        return tasks
    else:
        return {"tasks": []}

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file)

def display_tasks(tasks_listbox, tasks):
    tasks_listbox.delete(0, tk.END)
    if not tasks["tasks"]:
        tasks_listbox.insert(tk.END, "No tasks found.")
    else:
        for index, task in enumerate(tasks["tasks"], start=1):
            tasks_listbox.insert(tk.END, f"{index}. {task['title']} - {task['description']}")

def add_task(tasks, title, description):
    new_task = {"title": title, "description": description}
    tasks["tasks"].append(new_task)
    save_tasks(tasks)

def update_task(tasks, index, title, description):
    if 1 <= index <= len(tasks["tasks"]):
        tasks["tasks"][index - 1] = {"title": title, "description": description}
        save_tasks(tasks)
    else:
        messagebox.showwarning("Invalid Index", "Invalid task index.")

def delete_task(tasks, index):
    if 1 <= index <= len(tasks["tasks"]):
        del tasks["tasks"][index - 1]
        save_tasks(tasks)
    else:
        messagebox.showwarning("Invalid Index", "Invalid task index.")

def handle_add_button(entry_title, entry_description, tasks_listbox, tasks):
    title = entry_title.get()
    description = entry_description.get()
    if title and description:
        add_task(tasks, title, description)
        display_tasks(tasks_listbox, tasks)
        entry_title.delete(0, tk.END)
        entry_description.delete(0, tk.END)
    else:
        messagebox.showwarning("Missing Information", "Please enter both title and description.")

def handle_update_button(entry_index, entry_title, entry_description, tasks_listbox, tasks):
    try:
        index = int(entry_index.get())
        title = entry_title.get()
        description = entry_description.get()
        update_task(tasks, index, title, description)
        display_tasks(tasks_listbox, tasks)
        entry_index.delete(0, tk.END)
        entry_title.delete(0, tk.END)
        entry_description.delete(0, tk.END)
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid task index.")

def handle_delete_button(entry_index, tasks_listbox, tasks):
    try:
        index = int(entry_index.get())
        delete_task(tasks, index)
        display_tasks(tasks_listbox, tasks)
        entry_index.delete(0, tk.END)
    except ValueError:
        messagebox.showwarning("Invalid Input", "Please enter a valid task index.")

def main():
    tasks = load_tasks()

    root = tk.Tk()
    root.title("To-Do List")
    root.geometry("450x400")  

    tasks_listbox = tk.Listbox(root, width=50, height=10, bg="#f0f0f0", selectbackground="#a6a6a6")
    tasks_listbox.pack(pady=10)
    display_tasks(tasks_listbox, tasks)

    label_title = tk.Label(root, text="Title:")
    label_title.pack()

    entry_title = tk.Entry(root, width=50)
    entry_title.pack()

    label_description = tk.Label(root, text="Description:")
    label_description.pack()

    entry_description = tk.Entry(root, width=50)
    entry_description.pack()

    add_button = tk.Button(root, text="Add Task", command=lambda: handle_add_button(entry_title, entry_description, tasks_listbox, tasks), bg="#4caf50", fg="white")
    add_button.pack(pady=5)

    label_index = tk.Label(root, text="Task Index:")
    label_index.pack()

    entry_index = tk.Entry(root, width=50)
    entry_index.pack()

    update_button = tk.Button(root, text="Update Task", command=lambda: handle_update_button(entry_index, entry_title, entry_description, tasks_listbox, tasks), bg="#2196f3", fg="white")
    update_button.pack(pady=5)

    delete_button = tk.Button(root, text="Delete Task", command=lambda: handle_delete_button(entry_index, tasks_listbox, tasks), bg="#f44336", fg="white")
    delete_button.pack(pady=5)

    exit_button = tk.Button(root, text="Exit", command=root.destroy, bg="#607d8b", fg="white")
    exit_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
