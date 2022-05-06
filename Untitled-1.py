import turtle

#window Setup
wn = turtle.Screen()
wn.title("ratio of gasoline burnt and time spent")
wn.bgcolor("dark slate gray")
wn.setup(width=800,height=600)
wn.tracer(0)

# Below code for drawing rectangular upper body
car = turtle.Turtle()
car.color('#008000')
car.fillcolor('#008000')
car.penup()
car.goto(0,0)
car.pendown()
car.begin_fill()
car.forward(370)
car.left(90)
car.forward(50)
car.left(90)
car.forward(370)
car.left(90)
car.forward(50)
car.end_fill()
  
   
# Below code for drawing window and roof
car.penup()
car.goto(100, 50)
car.pendown()
car.setheading(45)
car.forward(70)
car.setheading(0)
car.forward(100)
car.setheading(-45)
car.forward(70)
car.setheading(90)
car.penup()
car.goto(200, 50)
car.pendown()
car.forward(49.50)
  
# Below code for drawing two tyres
car.penup()
car.goto(100, -10)
car.pendown()
car.color('#000000')
car.fillcolor('#000000')
car.begin_fill()
car.circle(20)
car.end_fill()
car.penup()
car.goto(300, -10)
car.pendown()
car.color('#000000')
car.fillcolor('#000000')
car.begin_fill()
car.circle(20)
car.end_fill()
car.hideturtle()
x = car.xcor()

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
    if minutes == 1:
        gallons = gallons + 0.00333333333 
        write.write("Gallons of gasoline used: {} Time in minutes spent: {}".format(gallons,minutes), align = "center", font= ("Corier", 24, "normal" )) 

