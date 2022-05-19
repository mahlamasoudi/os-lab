

class Shape:
    def __init__(self):
        self.enviroment=0
        self.area=0
    def printt(self):
        print("enviroment :",self.enviroment)
        print("aria :",self.area)
        

class Circle(Shape):
    def __init__(self,R):
        super().__init__()
        self.r=R

    def mohasebe(self):
        self.enviroment=2*3.14*self.r 
        self.area=3.14*self.r*self.r
        self.printt()  

class Rectangle(Shape):
    def __init__(self,X,Y):
        super().__init__()
        self.x=X
        self.y=Y

    def mohasebe(self):
        self.enviroment=(self.x+self.y)*2
        self.area=self.x*self.y
        self.printt()  


R=int(input("input radius of circle "))
newcircle=Circle(R)
newcircle.mohasebe()
X=int(input("input width of rectangle "))
Y=int(input("input length of rectangle "))
newrectangle=Rectangle(X, Y)
newrectangle.mohasebe()
       