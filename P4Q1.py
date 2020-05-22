class Shape:
    def area(self):
        self.area1=0

class Square(Shape):
    def __init__(self,length):
        self.length=length
    def area(self):
        print(self.length*self.length)
object=Square(int(input("Enter the length= ")))
object.area()