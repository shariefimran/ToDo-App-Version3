import json

def save_tasks(tasks):
    """ Save all tasks to a file"""
    with open("tasks.json",'w') as file:
        json.dump(tasks,file)




def load_tasks():
    """Load tasks from the file"""
    with open("tasks.json","r") as file:
        return json.load(file)


