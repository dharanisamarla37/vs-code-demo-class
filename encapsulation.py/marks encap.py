class students():
    def __init__(self,name,marks):
        self.name=name
        self.__marks=0
    def set_marks(self,marks):
        self.__marks=marks
        if (marks>=0) and(marks<=100):
            print("marks are valid")
        else:
            print("invalid marks")
    def get_marks(self):
        return self.__marks
s1 = students("Vicky",34)
s1.set_marks(34)            # Output: Marks updated
print(s1.get_marks())       # Output: 85
s1.set_marks(150)           # Output: Invalid marks
print(s1.get_marks())