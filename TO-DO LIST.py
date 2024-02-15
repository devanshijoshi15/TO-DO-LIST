import tkinter as tk

class ToDoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")
        self.root.configure(background="pink")  # Setting the background color to pink
        self.heading_label = tk.Label(self.root, text="TASK 1 - TO-DO LIST", font=("Arial", 16, "bold"))
        self.heading_label.pack(pady=10)
        self.tasks = []

        self.task_entry = tk.Entry(self.root, width=30)
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="gold", fg="black")
        self.add_button.pack(pady=5)

        self.task_list = tk.Listbox(self.root, width=50)
        self.task_list.pack(pady=15)

        self.remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task, bg="silver", fg="black")
        self.remove_button.pack(pady=5)

        self.update_button = tk.Button(self.root, text="Update Task", command=self.update_task, bg="white", fg="black")
        self.update_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Mark as Complete", command=self.mark_as_complete, bg="grey", fg="black")
        self.complete_button.pack(pady=5)

        self.exit_button = tk.Button(self.root, text="Exit", command=self.root.destroy, bg="red", fg="white")
        self.exit_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get()
        self.tasks.append((task, False))  # Storing task along with completion status
        self.update_task_list()

    def remove_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            task_index = selected_task[0]
            del self.tasks[task_index]
            self.update_task_list()

    def update_task(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            task_index = selected_task[0]
            updated_task = self.task_entry.get()
            self.tasks[task_index] = (updated_task, self.tasks[task_index][1])  # Preserve completion status
            self.update_task_list()

    def mark_as_complete(self):
        selected_task = self.task_list.curselection()
        if selected_task:
            task_index = selected_task[0]
            task, is_completed = self.tasks[task_index]
            self.tasks[task_index] = (task, True)  # Mark task as completed

            is_completed = not is_completed
            self.tasks[task_index] = (task, is_completed)

            # Update visual representation (with tick symbol)
            status = "✓" if is_completed else " "
            self.task_list.delete(task_index)  # Remove existing item
            self.task_list.insert(task_index, f"{status} {task}")  # Re-insert with updated status

            # Clear existing selection and reselect the updated task
            self.task_list.selection_clear(0, tk.END)
            self.task_list.selection_set(task_index)

    def update_task_list(self):
        self.task_list.delete(0, tk.END)
        for index, (task, is_completed) in enumerate(self.tasks, start=1):  # Enumerating tasks with numbering
            status = "✓" if is_completed else " "
            self.task_list.insert(tk.END, f"{index}. {task}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()
