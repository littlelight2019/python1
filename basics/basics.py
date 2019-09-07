class Animal(object):
    def __init__(self, name):
        self.name = "my name is %s, I am a " % name

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.name = "%s%s" % (self.name, "Dog")

class Cat(Animal):
    def __init__(self, name):
        self.name = "%s%s" % (name, "Cat")

class Person(object):
    def __init__(self, name):
        self.name = name
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        super(Employee, self).__init__(name)
        self.salary = salary

class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

if __name__ == '__main__':
    rover = Dog("Rover")
    satan = Cat("Satan")
    mary = Person("Mary")
    mary.pet = satan
    print(mary.pet.name)

    frank = Employee("Frank", 120000)
    frank.pet = rover
    print(frank.pet.name)

    flipper = Fish()
    crouse = Salmon()
    harry = Halibut()
