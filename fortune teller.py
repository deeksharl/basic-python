import turtle
import random
pointer = turtle.Turtle()
pointer.turtlesize(3,3,2)
pen = turtle.Turtle()
spin_amount = random.randint(1,360)
pen.penup()

#right side
pen.goto(200,0)
pen.pendown()
pen.write("yes!", font = ('open sans', 30))
pen.penup()

#left side
pen.goto(-400,0)
pen.pendown()
pen.write("absolutely not!",font = ('open sans', 30))
pen.penup()

#top side
pen.goto(-100, 300)
pen.pendown()
pen.write("uhh , may be ?",font = ('open sans', 30))
pen.penup()

#bottom side
pen.goto(0,-200)
pen.pendown()
pen.write("yes, but after 50 years!",font = ('open sans', 30) )
pen.ht()

pointer.left(spin_amount)
