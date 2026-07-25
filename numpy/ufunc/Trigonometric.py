import numpy as np

x = np.sin(np.pi/2)
print(x)


arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])

x2 = np.sin(arr)

print(x2)


# Convert Degrees Into Radians
arr2 = np.array([90, 180, 270, 360])

x3 = np.deg2rad(arr2)

print(x3)

# Radians to Degrees
arr3 = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
ax = np.rad2deg(arr3)

print(ax)

# Finding Angles
x4 = np.arcsin(1.0)
print(x4)

arr5 = np.array([1, -1, 0.1])

x5 = np.arcsin(arr5)

print(x5)


# Hypotenues
base = 3
prep = 4

x6 = np.hypot(base, prep)
print(x6)