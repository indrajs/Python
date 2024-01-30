class rectangle:
    def __init__(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        return self.length*self.breadth
    def perimeter(self):
        return 2*(self.length+self.breadth)
    def compare(self,others):
        if self.area()==others.area():
            print("two rectangle have same area")
        else:
            print("does not have same area")
rect1=rectangle(5,10)
rect2=rectangle(8,6)
print("area of rectangle1:",rect1.area())
print("perimeter of rectangle1:",rect1.perimeter())
print("area of rectangle2:",rect2.area())
print("perimeter of rectangle2:",rect2.perimeter())
rect1.compare(rect2)
