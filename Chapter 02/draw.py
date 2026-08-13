from vector_drawing import *
from vectors import *
from math import sqrt, sin, cos, pi

dino_vectors = [
  (6,4),(3,1),(1,2),(-1,5),(-2,5),
  (-3,4),(-4,4),(-5,3),(-5,2),(-2,2),
  (-5,1),(-4,0),(-2,1),(-1,0),(0,-3),
  (-1,-4),(1,-4),(2,-3),(1,-2),(3,-1),
  (5,1)
]

# draw(
#   Points(*dino_vectors),
#   Polygon(*dino_vectors)
# )

# draw(
#   Points(*[(x, x**2) for x in range(-10, 11)]),
#   grid=(1, 10),
#   nice_aspect_ratio=False
# )

# draw(
#   Points((2,2), (-1,3)),
#   Segment((2,2), (-1,3), color=red)
# )

# def hundred_dinos():
#   translations = [(12 * x, 10 * y) for x in range(-5 ,5) for y in range(-5, 5)]
#   dinos = [Polygon(*translate(t, dino_vectors), color=blue) for t in translations]
#   draw(*dinos, grid=None, axes=None, origin=None)

# hundred_dinos()

def add(*vectors):
  return (sum([v[0] for v in vectors]), sum([v[1] for v in vectors]))

def translate(translation, vectors):
  return [add(translation, v) for v in vectors]

def get_lengths():
  print(max(dino_vectors, key=length))

get_lengths()

def scale(vector, scalar):
  return [vector[0] * scalar, vector[1] * scalar]

def subtract(v1, v2):
  return (v1[0] - v2[0], v1[1] - v2[1])

def distance(v1, v2):
  displacement = subtract(v1, v2)
  return sqrt(displacement[0] ** 2 + displacement[1] ** 2)

def perimeter(vectors):
  length = len(vectors)
  distances = [distance(vectors[i], vectors[(i+1) % length]) for i in range(length)]
  return sum(distances)

print(perimeter(dino_vectors))

def to_cartesian(polar_vector):
  length, angle = polar_vector[0], polar_vector[1]
  return (length * cos(angle), length * sin(angle))

print(to_cartesian((5, (37 * pi)/180)))