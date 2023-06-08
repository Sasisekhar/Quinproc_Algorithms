from math import pi
from math import sin
val = 0
out = []
for i in range(0, 1024):
    val = val+(pi/512)
    out.append(float(format(sin(val), '0.6f')))

print(out)