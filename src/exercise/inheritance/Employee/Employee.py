class Employee :

    def __init__(self,name,ID, salary, department) -> None:
        self.name = name
        self.id = ID
        self.salary = salary
        self.department = department


    def get_info(self):
        return f"Name: {self.name}, ID: {self.id}, Salary: {self.salary}, Department: {self.department}"
