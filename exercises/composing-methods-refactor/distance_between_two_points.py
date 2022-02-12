# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.

import math

def calculate_point_dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)


xc1 = 4
yc1 = 4.25

xc2 = 53
yc2 = -5.35

# Calculate the distance between the two circle
distance = calculate_point_dist(xc1, yc1, xc2, yc2)
print('distance', distance)


# *** somewhere else in your program ***
xa = -36
ya = 97

xb = .34
yb = .91

# calcualte the length of vector AB vector which is a vector between A and B points.
length = calculate_point_dist(xa, ya, xb, yb)
print('length', length)
