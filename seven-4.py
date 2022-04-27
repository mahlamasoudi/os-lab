class complex():
    def __init__(self,r,im):
        self.real=r
        self.image=im


    def add(self,B):
        n=complex(0, 0)
        n.real=self.real+B.real
        n.image=self.image+B.image
        return n

    def sub(self,B):
        n=complex(0, 0)
        n.real=self.real-B.real
        n.image=self.image-B.image
        return n

    def multiply(self,B):
        n=complex(0, 0)
        n.real=(self.real*B.real-(self.image*B.image))
        n.image=(self.real*B.image+(self.image*B.real))
        return n

    def show(self):
        print(self.real,"+",self.image,"i")


print("which one do you want ?  1-add  2-sub 3-multiply")
select=int(input())
a=int(input("input real 1 -> "))
b=int(input("input image 1 -> "))
c=int(input("input real 2 -> "))
d=int(input("input image 2 -> "))
number1=complex(a, b)
number2=complex(c, d)
if select==1:
    output=number1.add(number2)
    output.show()
if select==2:
    output=number1.sub(number2)
    output.show()    
if select==3:
    output=number1.multiply(number2)
    output.show()        