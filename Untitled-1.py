import turtle

#window Setup
wn = turtle.Screen()
wn.title("ratio of gasoline burnt and time spent")
wn.bgcolor("dark slate gray")
wn.setup(width=800,height=600)
wn.tracer(0)

# Below code for drawing rectangular upper body
upperBody = turtle.Turtle()
upperBody.color('#008000')
upperBody.fillcolor('#008000')
upperBody.penup()
upperBody.goto(0,0)
upperBody.pendown()
upperBody.begin_fill()
upperBody.forward(370)
upperBody.left(90)
upperBody.forward(50)
upperBody.left(90)
upperBody.forward(370)
upperBody.left(90)
upperBody.forward(50)
upperBody.end_fill()
  
   
# Below code for drawing window and roof
carWindow = turtle.Turtle()
carWindow.goto(100, 50)
carWindow.pendown()
carWindow.setheading(45)
carWindow.forward(70)
carWindow.setheading(0)
carWindow.forward(100)
carWindow.setheading(-45)
carWindow.forward(70)
carWindow.setheading(90)
carWindow.penup()
carWindow.goto(200, 50)
carWindow.pendown()
carWindow.forward(49.50)
  
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

