import csv
import os
todo_file = "todo_list.csv"
def load_tasks():
    def load_tasks():
        if not os.path.exists(todo_file):
            return []
        with open(todo_file,"r") as file:
            reader = csv.reader(file)
            return list(reader)
        