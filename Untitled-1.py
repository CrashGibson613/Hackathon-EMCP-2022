import turtle

#window Setup
wn = turtle.Screen()
wn.title("ratio of gasoline burnt and time spent")
wn.bgcolor("dark slate gray")
wn.setup(width=800,height=600)
wn.tracer(0)

# Below code for drawing rectangular upper body
body = turtle.Turtle()
body.color('#008000')
body.fillcolor('#008000')
body.penup()
body.goto(0,0)
body.pendown()
body.begin_fill()
body.forward(370)
body.left(90)
body.forward(50)
body.left(90)
body.forward(370)
body.left(90)
body.forward(50)
body.end_fill()
  
   
# Below code for drawing window and roof
roof = turtle.Turtle()
roof.penup()
roof.goto(100, 50)
roof.pendown()
roof.setheading(45)
roof.forward(70)
roof.setheading(0)
roof.forward(100)
roof.setheading(-45)
roof.forward(70)
roof.setheading(90)
roof.penup()
roof.goto(200, 50)
roof.pendown()
roof.forward(49.50)
  
# Below code for drawing two tyres
tyres = turtle.Turtle()
tyres.penup()
tyres.goto(100, -10)
tyres.pendown()
tyres.color('#000000')
tyres.fillcolor('#000000')
tyres.begin_fill()
tyres.circle(20)
tyres.end_fill()
tyres.penup()
tyres.goto(300, -10)
tyres.pendown()
tyres.color('#000000')
tyres.fillcolor('#000000')
tyres.begin_fill()
tyres.circle(20)
tyres.end_fill()
tyres.hideturtle()
x = tyres.xcor()


#functions
def car_right():
    x = car.xcor()
    x = x - 20 
    car.setx(x) 

def car_left():
    x = car.xcor()
    x = x + 20 
    car.setx(x)

#keyboard bindings
wn.listen()
wn.onkeypress(car.left, "a")
wn.onkeypress(car.right, "d")

gallons = 0
minutes = 0

#write
write = turtle.Turtle()
write.speed(0)
write.goto(0,260)
write.shape("square")
write.color("white")
write.penup()
write.hideturtle()
write.write("Gallons of gasoline used: 0 Time in minutes spent: 0", align= "center", font=("Corier", 24, "normal"))

while True:
    time.sleep(60)
    gallons = gallons + 0.00333333333 
    minutes += 1
    write.write("Gallons of gasoline used: {} Time in minutes spent: {}".format(gallons,minutes), align = "center", font= ("Corier", 24, "normal" )) 

