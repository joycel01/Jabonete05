class Student:
    
    def __init__(self, name, age, course):
        
        self.name = name     
        self.age = age      
        self.course = course 

    
    def introduce(self):

        
        print(f"Hello, my name is {self.name}, {self.age} years old,  studying {self.course}.")
        


student1 = Student("Candice", 20, "Computer Science")  
student2 = Student("Shiloh", 22,  " Med Tech")  
student3 = Student("Ela", 21, "Architecture") 


print("Student 1:")
student1.introduce()
print("\nStudent 2:")
student2.introduce()
print("\nStudent 3:")
student3.introduce()