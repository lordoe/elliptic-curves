# EllipitcCurves

A small Python package for studying elliptic curves over finite fields.

## Installation

Clone repository and install requirements

```bash
pip install -r requirements.txt
```

## Example usage

```python
from ellipticcurves import EllipticCurve

# Define an elliptic curve y^2 = x^3 + 2x + 3 over F_97
curve = EllipticCurve(a=2, b=3, p=97)
print(curve)

# Retrieve and print all points on the curve
points = curve.get_points()
print(f"Number of points on the curve: {len(points)}")
for point in points:
    print(point)

# Perform point addition
P = curve.point(3, 6)
Q = curve.point(80, 10)
R = P + Q
print(f"P + Q = {R}")

# Perform scalar multiplication
k = 20
S = P * k
print(f"{k}P = {S}")

# Plot the curve
curve.plot()
```
