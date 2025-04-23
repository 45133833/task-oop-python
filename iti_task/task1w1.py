class Image:
    def __init__(self, url, alt):
        self.url = url
        self.alt = alt


class task:
    def __init__(self, title, description, image=None):
        self.title = title
        self.description = description
        self.image = image


class taskApp:
    def __init__(self):
        self.tasks = []

    def create(self, title, description):
        new_task=task(title,description)
        self.tasks.append(new_task)
        
        print("Create Task title is : {} and description is : {}".format(title, description))

    def read(self):
        for index,task  in enumerate(self.tasks):
            print(" index: {} title is : {} and description is : {}".format(index , task.title , task.description))

    def update(self, index, title, description):
        task =self.tasks[index]
            
        if title:
            task.title=title

        if description:
            task.description=description
        print('task updated')

        
        
    

    def delete(self, index):
       
        task =self.tasks.pop(index)
        print('task deleted')

        

# example usage 
app = taskApp()
app.create("Buy groceries", "Milk, Bread, Cheese")
app.create("Learn Python", "Complete OOP exercises")
app.read()
app.update(1, "Learn Advanced Python", "Complete OOP and Data Structures")
app.read()
app.delete(0)
app.read()


##############################################################
# remmber to uncomment this and comment the usage upper #
##############################################################

#app=taskApp()