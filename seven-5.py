class Time:
    def __init__(self,h,m,s):
        self.hour=h
        self.minute=m
        self.second=s


    def add(self,B):
        result=Time(0, 0, 0)
        result.second=self.second+B.second
        if result.second>=60:
            mb=int(result.second/60)
            result.second=result.second%60 
        else:
            mb=0
        result.minute=self.minute+B.minute
        result.minute+=mb
        if result.minute>=60:
            hb=int(result.minute/60)
            result.minute=result.minute%60  
        else:
            hb=0    
        result.hour=self.hour+B.hour
        result.hour+=hb 
        return result
#-------------------------------------------------------------
    def sub(self,B):
        result=Time(0, 0, 0)
        if self.hour>B.hour:
            result.second=self.second-B.second
            if result.second<0:
                self.minute-=1
                self.second+=60
                result.second=self.second-B.second
            result.minute=self.minute-B.minute
            if result.minute<0:
                self.hour-=1
                self.minute+=60
                result.minute=self.minute-B.minute
            result.hour=self.hour-B.hour
        elif B.hour>self.hour:
            result.second=B.second-self.second
            if result.second<0:
                B.minute-=1
                B.second+=60
                result.second=B.second-self.second
            result.minute=B.minute-self.minute
            if result.minute<0:
                B.hour-=1
                B.minute+=60
                result.minute=B.minute-self.minute
            result.hour=B.hour-self.hour
        elif self.hour==B.hour:
            if self.minute>B.minute:
                result.second=self.second-B.second
                if result.second<0:
                    self.minute-=1
                    self.second+=60
                    result.second=self.second-B.second
                result.minute=self.minute-B.minute
                result.hour=self.hour-B.hour  
            elif B.minute>self.minute:
                result.second=B.second-self.second
                if result.second<0:
                    B.minute-=1
                    B.second+=60
                    result.second=B.second-self.second   
                result.minute=B.minute-self.minute
                result.hour=B.hour-self.hour
            elif self.minute==B.minute:
                if self.second>B.second:
                    result.second=self.second-B.second
                    result.minute=self.minute-B.minute
                    result.hour=self.hour-B.hour
                elif B.minute>self.minute:
                    result.second=B.second-self.second
                    result.minute=B.minute-self.minute
                    result.hour=B.hour-self.hour 
                elif self.second==B.second:
                    result.second=0
                    result.minute=0
                    result.hour=0
        return result            
#---------------------------------------------------------------------
    def convertToTime(self,A):
        self.hour=int(A/3600)
        mb=A%3600
        self.minute=int(mb/60)
        self.second=mb%60
#-------------------------------------------------------------------
    def convertToSecond(self):
        second=self.hour*3600
        second=second+self.minute*60
        result=second+self.second
        return result
#----------------------------------------------------------------------
    def show(self):
        print(self.hour, ":",self.minute,":",self.second)    
#--------------------------------------------------------------------



print("which one do you want ?  1-add  2-sub 3-convert second to time 4-convert time to second")
select=int(input())
if select==1 or select==2:
    x1=int(input("input hour1 -> "))
    y1=int(input("input minute1 -> "))
    z1=int(input("input second1 -> "))
    x2=int(input("input hour2 -> "))
    y2=int(input("input minute2 -> "))
    z2=int(input("input second2 -> "))
    t1=Time(x1, y1, z1)
    t2=Time(x2, y2, z2)
    if select==1:
        output=t1.add(t2) 
        output.show()
    if select==2:
        output=t1.sub(t2)
        output.show() 
elif select==3:
    z1=int(input("input second -> "))
    t=Time(0,0,0)
    t.convertToTime(z1)
    t.show()
else:
    x1=int(input("input hour -> "))
    y1=int(input("input minute -> "))
    z1=int(input("input second -> "))  
    t=Time(x1, y1, z1)
    output=t.convertToSecond()
    print(output)