import math

class fraction:

    def __init__(self,n1,d1,n2,d2):
        self.numerator1=n1
        self.denominator1=d1
        self.numerator2=n2
        self.denominator2=d2
        if self.denominator1<0:
            self.numerator1*=-1
            self.denominator1*=-1
        if self.denominator2<0:
            self.numerator2*=-1
            self.denominator2*=-1


    def add(self):
        lcm=math.lcm(self.denominator1,self.denominator2)
        makhraj=lcm
        if self.denominator1==lcm and self.denominator2:
            surat=self.numerator1+self.numerator2
        if self.denominator1==lcm:
            surat=(self.numerator2*(int(lcm/self.denominator2)))+self.numerator1
        elif self.denominator2==lcm:
            surat=(self.numerator1*(int(lcm/self.denominator1)))+self.numerator2    
        else:
            surat=(self.numerator1*self.denominator2)+(self.numerator2*self.denominator1)
        self.show("add",surat,makhraj)
        

    def sub(self):
        lcm=math.lcm(self.denominator1,self.denominator2)
        makhraj=lcm
        if self.denominator1==lcm and self.denominator2:
            surat=self.numerator1-self.numerator2
        if self.denominator1==lcm:
            surat=self.numerator1-(self.numerator2*(int(lcm/self.denominator2)))
        elif self.denominator2==lcm:
            surat=(self.numerator1*(int(lcm/self.denominator1)))-self.numerator2    
        else:
            surat=(self.numerator1*self.denominator2)-(self.numerator2*self.denominator1)
        self.show("sub",surat,makhraj)    
        


    def mul(self):
        surat=self.numerator1*self.numerator2
        makhraj=self.denominator1*self.denominator2               
        self.show("multiply",surat,makhraj)

    def div(self):
        surat=self.numerator1*self.denominator2
        makhraj=self.denominator1*self.numerator2                
        self.show("division",surat,makhraj)

    def show(self,strresult,surat,makhraj):
        print("result of ",strresult,"->",surat,"/",makhraj)               

    def simplify(self):
        self.numerator1/self.denominator1
        self.show("simplify",surat,makhraj) 

x1=int(input("input numerator1 -> "))
y1=int(input("input denominator1 -> "))
x2=int(input("input numerator2 -> "))
y2=int(input("input denominator2 -> "))
obj=fraction(x1, y1, x2,y2)
print("which operation do you want ?  1-add  2-sub 3-multiplay 4-division")
select=int(input())
if select==1:
    obj.add()
if select==2:
    obj.sub()
if select==3:
    obj.mul()
if select==4:
    obj.div()         
if select==5:
    x=int(input("input numerator"))
    y=int(input("input denominator"))
    obj2=fraction(x, y,0, 0)    