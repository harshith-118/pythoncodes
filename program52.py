class Employee:
    def __init__(e,id,name):
        e.id=id
        e.name=name
    def display(e):
        print("Employee ID:",e.id,"Employee Name:",e.name)


emp=Employee(30385,"Harshith")
emp.display()
