from vectors import *
from draw2d import *
from draw3d import *

# draw3d(
#   Points3D((-1, -2, 2)),
#   Box3D(-1, -2, 2)
# )

coords = [(1, 1, 1), (-1, -1, -1), (1, -1, -1), (1, -1, 1), (1, 1, -1), (-1, -1, 1), (-1, 1, -1), (-1, 1, 1)]
draw3d(
  Points3D(*coords)
)