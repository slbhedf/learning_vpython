# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 16:02:25 2020

simulate_pendulum_small_width.py

assume theta << 1 
"""
from vpython import rate, box, sphere, vector, arrow, color, text, cylinder
from numpy import pi, cos, sin, sqrt

class Pendulum(object):
    def __init__(self, initial_theta, length):
        self.initial_theta =  initial_theta
        self.theta = initial_theta
        self.length = length
        self.time = 0.0
        self.time_step = 0.04
        self.g = 9.8
    def get_length(self):
        return self.length
    def get_theta(self):
        return self.theta
    def get_initial_theta(self):
        return self.initial_theta
    def width_is_small(self):
        return initial_theta < 1
    def update(self):
        self.time += self.time_step
        self.theta = self.initial_theta * cos(sqrt(self.g/self.length)*self.time)      
    def __str__(self):
        return "Pendulum <theta: " + str(self.theta) +  ", length: " + str(self.length) + ">" 
    
# draw X,Y,Z axes
x_axis = arrow(pos=vector(0,0,0), axis=vector(100,0,0), color=color.red, shaftwidth=3)
y_axis = arrow(pos=vector(0,0,0), axis=vector(0,100,0), color=color.yellow, shaftwidth=3)
z_axis = arrow(pos=vector(0,0,0), axis=vector(0,0,100), color=color.magenta, shaftwidth=3)

# draw x,y,z text at the end of the arrows
x_text = text(text=' x', pos=vector(100,0,0), color=x_axis.color, height=10)
y_text = text(text=' y', pos=vector(0,100,0), color=y_axis.color, height=10)
z_text = text(text=' z', pos=vector(0,0,100), color=z_axis.color, height=10)

# paramiter for
initial_theta = pi/6.0
theta = initial_theta
length = 10.0

# pendulum
pendulum = Pendulum(initial_theta, length)

# ceiling
ceiling = box(pos=vector(50,50,50), size=vector(50,0.1,50))

# ball 
x = 50 + length * sin(theta)
y = 50 - length * cos(theta)
z = 50
initial_position = vector(x, y, z)
ball_pos = initial_position
ball = sphere(pos=initial_position, raduis=1)

# rod
rod = cylinder(pos = ceiling.pos, axis = ball.pos - ceiling.pos, radius=0.1)

while(True):
    rate(25)
    pendulum.update() # 0.04 seconds forward
    theta = pendulum.get_theta() 
    x = 50 + length * sin(theta)
    y = 50 - length * cos(theta)
    z = 50
    ball_pos = vector(x, y, z)
    ball.pos = ball_pos
    rod.axis = ball_pos - ceiling.pos
    # print(pendulum)
    