class time:
    def __init__(self,h1,m1,s1,h2,m2,s2):
        self.hour1=h1
        self.hour2=h2
        self.minute1=m1
        self.minute2=m2
        self.second1=s1
        self.second2=s2

    def add(self):

        st=self.second1+self.second2
        if st>=60:
            mb=int(st/60)
            st=st%60 
        else:
            mb=0
        mt=self.minute1+self.minute2
        mt+=mb
        if mt>=60:
            hb=int(mt/60)
            mt=mt%60  
        else:
            hb=0    

        ht=self.hour1+self.hour2
        ht+=hb
        self.show("add",ht,mt,st)  

    def sub(self):
        if self.hour1>self.hour2:
            st=self.second1-self.second2
            if st<0:
                self.minute1-=1
                self.second1+=60
                st=self.second1-self.second2
            mt=self.minute1-self.minute2
            if mt<0:
                self.hour1-=1
                self.minute1+=60
                mt=self.minute1-self.minute2
            ht=self.hour1-self.hour2
        elif self.hour2>self.hour1:
            st=self.second2-self.second1
            if st<0:
                self.minute2-=1
                self.second2+=60
                st=self.second2-self.second1
            mt=self.minute2-self.minute1
            if mt<0:
                self.hour2-=1
                self.minute2+=60
                mt=self.minute2-self.minute1
            ht=self.hour2-self.hour1
        elif self.hour1==self.hour2:
            if self.minute1>self.minute2:
                st=self.second1-self.second2
                if st<0:
                    self.minute1-=1
                    self.second1+=60
                    st=self.second1-self.second2
                mt=self.minute1-self.minute2
                ht=self.hour1-self.hour  
            elif self.minute2>self.minute1:
                st=self.second2-self.second1
                if st<0:
                    self.minute2-=1
                    self.second2+=60
                    st=self.second2-self.second1
                    
                mt=self.minute2-self.minute1
                ht=self.hour2-self.hour1
            elif self.minute1==self.minute1:
                if self.second1>self.second2:
                    st=self.second1-self.second2
                    mt=self.minute1-self.minute2
                    ht=self.hour1-self.hour2
                elif self.minute2>self.minute1:
                    st=self.second2-self.second1
                    mt=self.minute2-self.minute1
                    ht=self.hour2-self.hour1 
                elif self.second1==self.second2:
                    st=0
                    mt=0
                    ht=0
        self.show("sub",ht,mt,st)        

    def converttotime(self):
        ht=int(self.second1/3600)
        mb=self.second1%3600
        mt=int(mb/60)
        st=mb%60
        print(ht,":",mt,":",st)

    def converttos(self):
        st=self.hour1*3600
        st=st+self.minute1*60
        st=st+self.second1
        print(st)
    def show(self,strresult,ht,mt,st):
        print("result of",strresult,"is -> ",ht,":",mt,":",st,)     

print("which one do you want ?  1-add  2-sub 3-convert second to time 4-convert time to second")
select=int(input())
if select==1 or select==2:
    x1=int(input("input hour1 -> "))
    y1=int(input("input minute1 -> "))
    z1=int(input("input second1 -> "))
    x2=int(input("input hour2 -> "))
    y2=int(input("input minute2 -> "))
    z2=int(input("input second2 -> "))
    obj=time(x1, y1, z1,x2,y2,z2)
    if select==1:
        obj.add() 
    if select==2:
        obj.sub()   
    
elif select==3:
    z1=int(input("input second1 -> "))
    obj1=time(0,0,0,z1,0,0,0)
    obj1.converttotime()
else:
    x1=int(input("input hour -> "))
    y1=int(input("input minute -> "))
    z1=int(input("input second -> "))  
    obj2=time(x1, y1, z1, 0, 0, 0)
