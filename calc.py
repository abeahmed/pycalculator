from turtle import Turtle
t=Turtle()
t.screen.title("calculator")
t.hideturtle()
t.pensize(5)
t.speed(0)
t.penup()
t.goto(150,150)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(225,30)
t.pendown()
t.write("+",align="center",font=("futura",100,"normal"))

t.penup()
t.goto(150,50)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(225,-50)
t.pendown()
t.write("-",align="center",font=("futura",100,"normal"))


t.penup()
t.goto(150,-50)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(225,-150)
t.pendown()
t.write("x",align="center",font=("futura",100,"normal"))

t.penup()
t.goto(150,-150)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(225,-270)
t.pendown()
t.write("÷",align="center",font=("futura",100,"normal"))


t.penup()
t.goto(0,150)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(75,60)
t.pendown()
t.write("3",align="center",font=("futura",50,"normal"))



t.penup()
t.goto(0,50)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(75,-40)
t.pendown()
t.write("6",align="center",font=("futura",50,"normal"))



t.penup()
t.goto(0,-50)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(75,-130)
t.pendown()
t.write("9",align="center",font=("futura",50,"normal"))



t.penup()
t.goto(0,-150)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(75,-230)
t.pendown()
t.write("=",align="center",font=("futura",50,"bold"))



t.penup()
t.goto(-150,150)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(-75,60)
t.pendown()
t.write("2",align="center",font=("futura",50,"normal"))



t.penup()
t.goto(-150,50)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(-75,-40)
t.pendown()
t.write("5",align="center",font=("futura",50,"normal"))


t.penup()
t.goto(-150,-50)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(-75,-130)
t.pendown()
t.write("8",align="center",font=("futura",50,"normal"))


t.penup()
t.goto(-150,-150)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(-75,-230)
t.pendown()
t.write("0",align="center",font=("futura",50,"normal"))


t.penup()
t.goto(-300,150)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(-225,60)
t.pendown()
t.write("1",align="center",font=("futura",50,"normal"))


t.penup()
t.goto(-300,50)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(-225,-40)
t.pendown()
t.write("4",align="center",font=("futura",50,"normal"))


t.penup()
t.goto(-300,-50)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(-225,-130)
t.pendown()
t.write("7",align="center",font=("futura",50,"normal"))


t.penup()
t.goto(-300,-150)
t.pendown()
for steps in range(2):
    t.fd(150)
    t.right(90)
    t.fd(100)
    t.right(90)
t.penup()
t.goto(-225,-230)
t.pendown()
t.write("C",align="center",font=("futura",50,"normal"))

t.penup()
t.goto(-300,300)
t.pendown()
for steps in range(2):
    t.fd(600)
    t.right(90)
    t.fd(100)
    t.right(90)



num = ""
num2 =""
display=""
symbol=""
oper = False
number=False
equal=False
result=0.0

def handleClick(x,y):
    global num
    global oper
    global number
    global equal
    global num2
    global display
    global symbol
    global result
    if x>5 and x<150 and y>52 and y<149 and oper==False  and equal==False :
        display=display+"3"
        num=num+"3"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True       
    if x>1 and x<150 and y>-50 and y<48 and oper==False  and equal==False :
        display=display+"6"
        num=num+"6"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>0 and x<150 and y>-147 and y<-48 and oper==False  and equal==False :
        display=display+"9"
        num=num+"9"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>-150 and x<0 and y>51 and y<149 and oper==False  and equal==False :
        display=display+"2"
        num=num+"2"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>-150 and x<0 and y<50 and y>-50 and oper==False  and equal==False :
        display=display+"5"
        num=num+"5"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>-150 and x<0 and y<-50 and y>-150 and oper==False  and equal==False :
        display=display+"8"
        num=num+"8"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>-150 and x<0 and y<-150 and y>-250 and oper==False  and equal==False :
        display=display+"0"
        num=num+"0"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>-300 and x<-150 and y<150 and y>50 and oper==False  and equal==False:
        display=display+"1"
        num=num+"1"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>-300 and x<-150 and y<50 and y>-50  and oper==False  and equal==False:
        display=display+"4"
        num=num+"4"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>-300 and x<-150 and y<-50 and y>-150  and oper==False  and equal==False:
        display=display+"7"
        num=num+"7"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True

    if x>150 and x<300 and y<150 and y>50 and oper==False and number==True  and equal==False:
        display=display+"+"
        symbol="+"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))      
        oper=True
    elif x>150 and x<300 and y<50 and y>-50 and oper==False and number==True  and equal==False:
        display=display+"-"
        symbol="-"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        oper=True
    elif x>150 and x<300 and y<-50 and y>-150 and oper==False and number==True  and equal==False:
        display=display+"x"
        symbol="x"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        oper=True
    elif x>150 and x<300 and y<-150 and y>-250 and oper==False and number==True  and equal==False:
        display=display+"÷"
        symbol="÷"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        oper=True
    elif x>-300 and x<-150 and y<-150 and y>-250 and number==True:
        t.color("white")
        t.penup()
        t.goto(-295,295)
        t.pendown()
        t.begin_fill()
        for steps in range(2):
              t.fd(590)
              t.right(90)
              t.fd(90)
              t.right(90)
        t.end_fill()
        t.color("black")
        display=""
        num=""
        num2=""
        oper=False
        equal=False
        
            
    if x>5 and x<150 and y>52 and y<149 and oper==True  and equal==False :
        num2=num2+"3"
        display=display+"3"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True       
    if x>1 and x<150 and y>-50 and y<48 and oper==True  and equal==False :
        num2=num2+"6"
        display=display+"6"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>0 and x<150 and y>-147 and y<-48 and oper==True  and equal==False :
        num2=num2+"9"
        display=display+"9"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>-150 and x<0 and y>51 and y<149 and oper==True  and equal==False :
        num2=num2+"2"
        display=display+"2"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>-150 and x<0 and y<50 and y>-50 and oper==True  and equal==False :
        num2=num2+"5"
        display=display+"5"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>-150 and x<0 and y<-50 and y>-150 and oper==True  and equal==False :
        num2=num2+"8"
        display=display+"8"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>-150 and x<0 and y<-150 and y>-250 and oper==True  and equal==False :
        num2=num2+"0"
        display=display+"0"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>-300 and x<-150 and y<150 and y>50 and oper==True  and equal==False:
        num2=num2+"1"
        display=display+"1"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>-300 and x<-150 and y<50 and y>-50 and oper==True   and equal==False:
        num2=num2+"4"
        display=display+"4"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True
    if x>-300 and x<-150 and y<-50 and y>-150 and oper==True   and equal==False:
        num2=num2+"5"
        display=display+"5"
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        number=True

    
    
    if x>0 and x<150 and y<-150 and y>-250 and equal==False and number==True:
        t.penup()
        t.goto(-270,200)
        t.pendown()
        t.write(display,font=("futura",50,"normal"))
        t.color("white")
        t.penup()
        t.goto(-295,295)
        t.pendown()
        t.begin_fill()
        for steps in range(2):
              t.fd(590)
              t.right(90)
              t.fd(90)
              t.right(90)
        t.end_fill()
        t.color("black")
        equal=True
        if symbol=="+":
            result=float(num)+float(num2)
        if symbol=="-":
            result=float(num)-float(num2)
        if symbol=="x":
            result=float(num)*float(num2)
        if symbol=="÷":
            result=float(num)/float(num2)
        t.penup()
        t.goto(-270,200)
        t.pendown()
        result2 = str(result)
        if result2.endswith(".0"):
            result2 = result2.replace(".0","")
        t.write(result2,font=("futura",50,"normal"))
        display=""
        num=""
        num2=""
        oper=False
        equal=False
        num=str(result)
        display=str(result2)
       
    



t.screen.onclick(handleClick)



t.screen.mainloop()