import turtle

t = turtle.Turtle()

def tree(d,x1,y1):
   #d is the depth

   if d==0: #base case
       return 0

   a = t.Turtles()
   b = t.Turtle()

   a.penup()
   b.penup()

   a.goto(x1,y1)
   b.goto(x1,y1) # move to the correct position

   a.pendown()
   b.pendown()

   a.left(45)
   b.right(45)
   a.forward(10*(2**d)) 
   b.forward(10*(2**d))

   ax,ay = a.pos() #get position of new turtles
   bx,by = b.pos()

   tree(d-1,ax,ay)  #recurse top branch
   tree(d-1,bx,by)  #recurse bottom branch