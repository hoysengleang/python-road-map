import Employee

class Developer(Employee.Employee):

    def __init__(self, name, ID, salary, department, programming_language, position) -> None:
        super().__init__(name, ID, salary, department)
        self.programming_language = programming_language
        self.position = position
        
    def get_info(self):
        return f"{super().get_info()} - Programming Language: {self.programming_language}"

    def calculate_salary(self):
        return self.salary * 12
    
    def calculate_bonus(self):
        if self.programming_language.lower() == "python" and self.department.lower() == "IT" and self.position.lower() == "Senior":
            return self.salary * 0.2
        else:
            return self.salary * 0.1



if __name__ == "__main__":
    developer = Developer("John Doe", 1234567890, 100000, "IT", "Python", "Senior")
    print(developer.get_info())
    print(developer.calculate_salary())
    print(developer.calculate_bonus())