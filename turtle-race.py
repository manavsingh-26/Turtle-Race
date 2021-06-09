import turtle as t
import random

race_is_on=False
screen = t.Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet",prompt="Which turtle will win race?Enter color")

turtles = []
colors = ["red","blue","green","yellow","orange","violet"]
add=0
for i in range(0,6):
    new_turtle = t.Turtle(shape = "turtle")
    new_turtle.penup()
    new_turtle.color(colors[i])
    new_turtle.goto(x=-230,y=-100+add)
    add+=50
    turtles.append(new_turtle)

if user_bet:
    race_is_on =True

while race_is_on:
    
    for turtle in turtles:
        if turtle.xcor()>230:
            race_is_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won the bet, {winning_color} turtle won the race")
            else:
                print(f"You lost the bet, {winning_color} turtle won the race")
        distance = random.randint(0,10)
        turtle.forward(distance)
    

    
    



screen.exitonclick()