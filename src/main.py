import json
import os

TODO_FILE = "tasks.json"


def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []


def save_tasks(data):
    with open(TODO_FILE, "w") as f:
        json.dump(data, f, indent=2)


def show_tasks(data):
    if not data:
        print("No tasks found.")
        return
    print("\nyour tasks:")
    for i, task in enumerate(data, 1):
        status = "done" if task.get("completed") else " "
        print(f"{i}.[{status}] {task['title']}")
    print()


def add_task(data, title):
    data.append({"title": title, "completed": False})
    save_tasks(data)
    print(f"tasks added :{title}")


def complete_task(data, task_id):
    if 1 <= task_id <= len(data):
        data[task_id - 1]["completed"] = True
    else:
        print("Task ID Invalid")


def main():
    loaded_tasks = load_tasks()
    while True:
        print("\nWelcome to ToDo App")
        print("1.Show all tasks")
        print("2.Add a task")
        print("3.Complete a task")
        print("4.Exit")

        user_choice = input("\nEnter your choice(1-4): ")
        if user_choice == "1":
            show_tasks(loaded_tasks)
        elif user_choice == "2":
            todo_title = input("Enter task title: ")
            add_task(data=loaded_tasks, title=todo_title)


if __name__ == "__main__":
    main()
