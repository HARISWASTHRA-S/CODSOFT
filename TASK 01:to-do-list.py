import tkinter as tk
from tkinter import messagebox
import json


TASKS_FILE = "tasks.json"


def load_tasks():
    try:
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

# Save 
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add 
def add_task():
    description = task_entry.get().strip()
    due_date = due_date_entry.get().strip()
    if description:
        tasks.append({"description": description, "due_date": due_date, "completed": False})
        save_tasks()
        refresh_task_list()
        task_entry.delete(0, tk.END)
        due_date_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Task description cannot be empty!")

# Refresh 
def refresh_task_list():
    pending_listbox.delete(0, tk.END)
    completed_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks):
        task_text = f"{task['description']} (Due: {task['due_date']})" if task['due_date'] else task['description']
        if task["completed"]:
            completed_listbox.insert(tk.END, f"{i + 1}. {task_text}")
        else:
            pending_listbox.insert(tk.END, f"{i + 1}. {task_text}")

# Mark as completed
def mark_task_completed():
    selected_index = pending_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        tasks[index]["completed"] = True
        save_tasks()
        refresh_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed!")

# Delete 
def delete_task():
    selected_index = pending_listbox.curselection() or completed_listbox.curselection()
    if selected_index:
        index = selected_index[0]
        tasks.pop(index)
        save_tasks()
        refresh_task_list()
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete!")


tasks = load_tasks()


root = tk.Tk()
root.title("To-Do List Application")  #main window
root.geometry("500x500")


input_frame = tk.Frame(root)
input_frame.pack(pady=10)

task_label = tk.Label(input_frame, text="Task:")
task_label.grid(row=0, column=0, padx=5, pady=5)
task_entry = tk.Entry(input_frame, width=40)
task_entry.grid(row=0, column=1, padx=5, pady=5)

due_date_label = tk.Label(input_frame, text="Due Date (optional):")
due_date_label.grid(row=1, column=0, padx=5, pady=5)
due_date_entry = tk.Entry(input_frame, width=40)
due_date_entry.grid(row=1, column=1, padx=5, pady=5)

add_task_button = tk.Button(input_frame, text="Add Task", command=add_task)
add_task_button.grid(row=2, columnspan=2, pady=10)

# Task List Frame
task_frame = tk.Frame(root)
task_frame.pack(pady=20)

# Pending Tasks
pending_label = tk.Label(task_frame, text="Pending Tasks", font=("Arial", 12))
pending_label.grid(row=0, column=0)
pending_listbox = tk.Listbox(task_frame, width=40, height=10)
pending_listbox.grid(row=1, column=0, padx=10, pady=10)

# Completed Tasks
completed_label = tk.Label(task_frame, text="Completed Tasks", font=("Arial", 12))
completed_label.grid(row=0, column=1)
completed_listbox = tk.Listbox(task_frame, width=40, height=10)
completed_listbox.grid(row=1, column=1, padx=10, pady=10)


action_frame = tk.Frame(root)
action_frame.pack(pady=10)

mark_completed_button = tk.Button(action_frame, text="Mark as Completed", command=mark_task_completed)
mark_completed_button.grid(row=0, column=0, padx=10)

delete_task_button = tk.Button(action_frame, text="Delete Task", command=delete_task)
delete_task_button.grid(row=0, column=1, padx=10)


refresh_task_list()

root.mainloop()
