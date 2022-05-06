import turtle

#car
car = turtle.Turtle
car.shape("square")
car.color("indian red")
car.shapesize(stretch_wid = 4, stretch_len=10)

#window Setup
wn = turtle.Screen()
wn.title("ratio of gasoline burnt and time spent")
wn.color("dark slate gray")
wn.setup(width=800,height=600)
wn.tracer(0)

gallons = 0
minutes = 0

#write
write = turtle.Turtle()
write.goto(0,260)
write.penup()
write.write("Gallons of gasoline used: 0 Time in minutes spent: 0", align= "center", font=("Corier", 24, "normal"))

if minutes == 1:
    gallons = gallons + 0.00333333333 
    write.write("Gallons of gasoline used: {} Time in minutes spent: {}".format(gallons,minutes), align = "center", font= ("Corier", 24, "normal" )) 

