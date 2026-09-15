import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.cm
from vectors import *
from math import *
from vectors import scale, add

# def compose(f1, f2):
#   def new_function(input):
#     return f1(f2(input))
#   return new_function

def polygon_map(transformation, polygons):
  return [[transformation(vertex) for vertex in triangle] for triangle in polygons]

def compose(*args):
  def new_function(input):
    state = input
    for f in reversed(args):
      state = f(state)
    return state
  return new_function

def prepend(string):
  def new_function(input):
    return string + input
  return new_function

f = compose(prepend("P"), prepend("y"), prepend("t"))

def curry2(func):
  def a_function(arg1):
    def b_function(arg2):
      return func(arg1, arg2)
    return b_function
  return a_function

scale_by = curry2(scale)

def stretch_x(scalar, vector):
  x, y, z = vector
  return scalar * x, y, z

stretch_x_by = curry2(stretch_x)

print(stretch_x_by(2)((1,2,3)))

# print(f('hon'))