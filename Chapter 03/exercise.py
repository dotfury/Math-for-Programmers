from vectors import *
from draw2d import *
from draw3d import *
from math import sqrt, acos

# draw3d(
#   Points3D((-1, -2, 2)),
#   Box3D(-1, -2, 2)
# )

# pm1 = [1,-1]
# vertices = [(x,y,z) for x in pm1 for y in pm1 for z in pm1]
# edges = [((-1,y,z),(1,y,z)) for y in pm1 for z in pm1] +\
# [((x,-1,z),(x,1,z)) for x in pm1 for z in pm1] +\
# [((x,y,-1),(x,y,1)) for x in pm1 for y in pm1]
# draw3d(
#   Points3D(*vertices,color=blue),
#   *[Segment3D(*edge) for edge in edges]
# )

def length(v):
  return sqrt(sum([c ** 2 for c in v]))

# vertices = [(4,0,3), (-1,0,1)]
# draw3d(
#   Arrow3D((4, 0, 3))
# )

def dot(u, v):
  return sum([coord1 * coord2 for coord1, coord2 in zip(u, v)])

# print(dot((-1,-1,1), (1,2,1)))

def angle_between(v1, v2):
  return acos(dot(v1, v2) / (length(v1) * length(v2)))

def cross(u, v):
  ux, uy, uz = u
  vx, vy, vz = v
  return (uy * vz - uz * vy, uz * vx - ux * vz, ux * vy - uy * vx)

print(cross((0,0,1), (2,2,2)))