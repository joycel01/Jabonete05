class Car:
   
    def __init__(self, brand, model, year):
        
        self.brand = brand
        self.model = model  
        self.year = year     
    
    
    def display_info(self):
       
        print("Car Details:")
        print(f"Brand: {self.brand}")  
        print(f"Model: {self.model}")  
        print(f"Year: {self.year}") 
        print("----------------------------")  


car1 = Car("Lamborghini", "350 GT", 1964)

car2 = Car("McLaren", "F1", 1992)


car1.display_info()  
car2.display_info()