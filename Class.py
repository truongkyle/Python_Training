class Person:
    count = 0 # class atribute
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Person.count +=1
    def show_info(self):
        print(f"{self.name} : {self.age}")
        return

class Student(Person):
    def __init__(self, name, age, class_number):
        super().__init__(name, age)
        self.class_number = class_number
    def show_info(self):
        print(self.name, self.age, self.class_number)


def main():
    per_1 = Student("Van", 23, 4)
    print(f"number of person: {Person.count}")
    per_1.show_info()

if __name__ == "__main__":
    main()