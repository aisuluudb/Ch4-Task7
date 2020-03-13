class Student():
    """Student Information"""

    def __init__(self, name, age, major):
        self.name = name
        self.age = age
        self.major = major
    
    def __str__(self):
        return f'name: {self.name}, age: {self.age}, major: {self.major}'
    
steve = Student('Steven Schultz', 23, 'English')
johnny = Student('Jonathan Rosenberg', 24, 'Biology')
penny = Student('Penelope Meramveliotakis', 21, 'Physics')
print(steve)
print(johnny)
print(penny)
