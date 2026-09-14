from teapot import load_triangles
from draw_model import draw_model
from vectors import scale, add

####################################################################
#### this code takes a snapshot to reproduce the exact figure 
#### shown in the book as an image saved in the "figs" directory
#### to run it, run this script with command line arg --snapshot
import sys
import camera
if '--snapshot' in sys.argv:
    camera.default_camera = camera.Camera('fig_4.4_draw_teapot',[0])
####################################################################

def scale_by(scalar):
  def new_function(input):
    return scale(scalar, input)
  return new_function

def translate_by(vector):
  def new_function(input):
    return add(vector, input)
  return new_function

scale_2 = scale_by(2)
translate_left_1 = translate_by((-1, 0, 0))

def compose(f1, f2):
  def new_function(input):
    return f1(f2(input))
  return new_function

def polygon_map(transformation, polygons):
  return [[transformation(vertex) for vertex in triangle] for triangle in polygons]

scale_and_translate = compose(scale_2, translate_left_1)
translate_20 = translate_by((0, 0, -20))
scale_half = scale_by(0.5)
scale_negative = scale_by(-1)

scale_small = scale_by(0.4)
scale_large = scale_by(1.5)

scale_and_scale = compose(scale_small, scale_large)

original = load_triangles()
modified = polygon_map(scale_and_scale, original)

draw_model(modified)