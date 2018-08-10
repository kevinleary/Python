# Copyright 2017, 2013, 2011 Pearson Education, Inc., W.F. Punch & R.J.Enbody
# Draw Sierpinski figure

import turtle
import tkinter
from PIL import Image
import os
import glob
import string
import random

def sierpinski(t, length, depth): 
    if depth > 1:
        t.dot()  # mark position to better see recursion
    if depth == 0:       # base case
        t.stamp() # stamp a triangular shape
    else:
        t.forward(length)
        sierpinski(t,length/2, depth-1)  # recursive call
        t.backward(length)
        t.left(120)
        t.forward(length)
        sierpinski(t,length/2, depth-1)   # recursive call
        t.backward(length)
        t.left(120)
        t.forward(length)
        sierpinski(t,length/2, depth-1)  # recursive call
        t.backward(length)
        t.left(120)

def compute(width_int, height_int, length_int, depth_int):
    ''' Complicated, but here is the deal:
    1) create a window, root, with nothing in it. We have control of the window this way
    2) grab the canvas (drawing surface) from root
    3) use that canvas for our Turtle screen
    4) make a raw turtle on the screen we just made from the root canvas
    5) withdraw (hide) the window. You might still get a flash of the window.
       Must be after the turtle creation as no object stuff can occur after a withdraw.
       Drawing window now hidden
    6) go fast: no delay, no tracing at all, only draw once, full dump, at the end with update
    7) do the random file thing, clean out the old files in static (make static dir if necessary)
    8) dump the canvas as a postscript file, our only option
    9) convert eps file to png using PIL
    '''
    
    root = tkinter.Tk()
    canv = tkinter.Canvas(root, width=width_int, height=height_int)    
    scr = turtle.TurtleScreen(canv)
    canv.pack()
    t = turtle.RawTurtle(scr)
    root.withdraw()            

    # draw as fast as possible
    scr.delay(0)
    scr.tracer(0,0)

    ##### actually do some turtle drawing with a function #####
    sierpinski(t, length_int, depth_int)

    # one update of the screen/canvas, all drawing done here and all at once
    scr.update()
    
    if not os.path.isdir('static'):
        os.mkdir('static')
    else:
        f_eps = "static/sier.eps"
        # new random file name, so browser won't cache it
        f_png = "static/" + ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(8)) + ".png"        

        # Remove old plot files
        for filename in glob.glob(os.path.join('static', '*')):
            os.remove(filename)
        # dump the screen as postscript, our only option from a canvas unfortunately    
        canv.postscript(file=f_eps)
        # remove the window, we're done
        root.destroy()
        # use PIL to convert eps to png
        im = Image.open(f_eps)
        im.save(f_png)
        return f_png

if __name__ == "__main__":
    compute(900, 800, 200, 6)    
