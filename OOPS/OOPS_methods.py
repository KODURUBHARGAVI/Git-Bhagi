class Mainclass:
    Institute='IIT Madras'
    specialization='Industrail AI'
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def get_name_age(self):
        #Instance method--> takes instance(self) as the first parameter
        print(f"Student named: {self.name} having age: {self.age} from {Mainclass.Institute}")

    @classmethod
    def access_class_variables(cls, change_company):
        #Class method--> takes class(cls) as the first parameter-->used to access/modify class variables 
        #cls.Institute=change_company
        print(f"Accessing common details:: {cls.Institute}")

    @staticmethod
    def static_method_example():
        #Static method--> doesn't take instance or class as the first parameter-->used for utility functions
        print("I am a static method")
        
obj1=Mainclass("Bhargavi",26)
obj1.get_name_age()
Mainclass.access_class_variables("IITG")
obj1.get_name_age()
Mainclass.static_method_example()
obj1.static_method_example()
print('abc')