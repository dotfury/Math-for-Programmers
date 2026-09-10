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

def scale2(v):
  return scale(2.0, v)

def translate_left(v):
  return add((-1, 0, 0), v)

original = load_triangles()
modified = [[translate_left(scale2(x)) for x in tri] for tri in original]

draw_model(modified)