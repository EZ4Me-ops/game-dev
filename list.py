tasks=[]
while True:
    print("--- TO DO LIST ---" )
    print("1.View tasks ")
    print("2.add a task")
    print("3.remove a task")
    print("4.update the tasks")
    print("5.exit")
    user=input("please pick a option from 1-5 ")

    if user=="1":
        for task in tasks:
            print(task)
    elif user=="2":
        add=input("type the task you want to add ")
        tasks.append(add)

    elif user=="3":
        delete=input("what do you want to remove? ")
        tasks.remove(delete)