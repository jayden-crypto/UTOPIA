from datetime import datetime

class Task:
    def __init__(self, description, due_date=None):
        self.description = description
        self.due_date = due_date

class TodoList:
    def __init__(self):
        self.tasks = []

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in your student planner, take a break and relax!")
        else:
            print("\nStudent Planner - To Do List:")
            print("+------+-------------------------------+---------------------+")
            print("| Index|         Task Description      |       Due Date      |")
            print("+------+-------------------------------+---------------------+")
            for index, task in enumerate(self.tasks, start=1):
                due_date_str = task.due_date.strftime('%d-%m-%Y') if task.due_date else "Not set"
                print(f"|  {index:3} | {task.description:30}| {due_date_str:19} |")
            print("+------+-------------------------------+---------------------+")

    def parse_date(self, date_str):
        try:
            return datetime.strptime(date_str, '%d-%m-%Y')
        except ValueError:
            print("Invalid date format. Task will be created without due date.")
            return None

    def create_task(self, description):
        due_date_str = input("Enter the due date (dd-mm-yyyy format, press Enter if not set): ")
        if due_date_str:
            due_date = self.parse_date(due_date_str)
        else:
            due_date = None
        new_task = Task(description, due_date)
        self.tasks.append(new_task)
        print(f"\nNew task '{description}' successfully added to your planner.")

    def delete_task(self, task_index):
        try:
            task_index = int(task_index)
            if 1 <= task_index <= len(self.tasks):
                deleted_task = self.tasks.pop(task_index - 1)
                print(f"\nKudos! on completing the task '{deleted_task.description}', it has been removed successfully")
            else:
                print("\nInvalid task index, please try again.")
        except ValueError:
            print("\nInvalid input, please enter a valid task index.")


def main():
    print("Welcome to your Student Planner!")
    todo_list = TodoList()

    while True:
        print("\nOptions: ")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")

        choice = input("What would you like to do? (1/2/3/4): ")

        chosen_option = choice

        if chosen_option == "1":
            todo_list.view_tasks()
        elif chosen_option == "2":
            description = input("Enter the task description: ")
            todo_list.create_task(description)
        elif chosen_option == "3":
            task_index = input("Enter the task index you wish to remove: ")
            todo_list.delete_task(task_index)
        elif chosen_option == "4":
            print("\nPeace out!")
            break
        else:
            print("\nInvalid input, please eneter a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
