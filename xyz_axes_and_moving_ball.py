'''
xyz_axes_and_moving_ball.py
 This file was created on 21 Feb 2020.

3D graphics will be displayed on your defalt browser.

Ctrl-drag: change angle
mouse scroll: Zoom in or out

# arrow https://www.glowscript.org/docs/VPythonDocs/arrow.html
# sphere https://www.glowscript.org/docs/VPythonDocs/sphere.html
# rate https://www.glowscript.org/docs/VPythonDocs/rate.html
# attach_trail https://www.glowscript.org/docs/VPythonDocs/trail.html
# text https://www.glowscript.org/docs/VPythonDocs/text.html

'''

from vpython import arrow, sphere, color, vector, rate, attach_trail, text
from numpy import sin, cos

t = 0.0 # time
dt = 0.01 # delta time
r = 100 # ball moves on a circle whose radius is 100

# draw X,Y,Z axes
x_axis = arrow(pos=vector(0,0,0), axis=vector(100,0,0), color=color.red, shaftwidth=3)
y_axis = arrow(pos=vector(0,0,0), axis=vector(0,100,0), color=color.yellow, shaftwidth=3)
z_axis = arrow(pos=vector(0,0,0), axis=vector(0,0,100), color=color.magenta, shaftwidth=3)

# draw x,y,z text at the end of the arrows
x_text = text(text=' x', pos=vector(100,0,0), color=x_axis.color, height=10)
y_text = text(text=' y', pos=vector(0,100,0), color=y_axis.color, height=10)
z_text = text(text=' z', pos=vector(0,0,100), color=z_axis.color, height=10)

# moving ball
ball = sphere(pos=vector(r*cos(t),r*sin(t),0), radius=10, color=color.blue)
direction = arrow(pos=ball.pos, axis=vector(-r*sin(t), r*cos(t),0)*0.25, color=color.cyan, shaftwidth=3)

# leave trail after ball moves
attach_trail(ball, color=ball.color, radius=0.1*ball.radius, type="curve", retain=100)

# ball moves
while t < 100:
    rate(25) # wait 1/25 seconds. approximately 25fps animation
    ball.pos = vector(r*cos(t), r*sin(t), 0)
    direction.pos = ball.pos
    direction.axis = vector(-r*sin(t), r*cos(t), 0) * 0.25
    t += dt
    