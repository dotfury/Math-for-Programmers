import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import matplotlib.cm
from vectors import *
from math import *

def compose(f1, f2):
  def new_function(input):
    return f1(f2(input))
  return new_function

def polygon_map(transformation, polygons):
  return [[transformation(vertex) for vertex in triangle] for triangle in polygons]