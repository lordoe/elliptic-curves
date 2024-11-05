import matplotlib.pyplot as plt
from .point import Point

class EllipticCurve:
    def __init__(self, a, b, p):
        """
        Initialize an elliptic curve of the form y^2 = x^3 + ax + b over the finite field F_p.
        
        Parameters:
            a (int): Coefficient of x.
            b (int): Constant term.
            p (int): Prime number defining the field F_p.
        
        Raises:
            ValueError: If the curve is singular (i.e., 4a^3 + 27b^2 ≡ 0 mod p).
        """
        if (4*a**3 + 27*b**2) % p == 0:
            raise ValueError('Elliptic curve is not non-singular')
        self.a = a
        self.b = b
        self.p = p
        self.points = self._calc_points()

    def point(self, x, y):
        return Point(x, y, self)
    
    def get_points(self):
        return self.points

    def _calc_points(self):
        points = [Point(None, None, self)]
        y_s = [y for y in range(self.p)]
        y_sqares = [y**2 % self.p for y in range(self.p)]
        for x in range(self.p):
            x3_ax_b = (x**3 + self.a*x + self.b) % self.p
            for y, y2 in zip(y_s, y_sqares):
                if y2 == x3_ax_b:
                    points.append(self.point(x, y))
        return points
    
    def __str__(self):
        return f"y^2 = x^3 + {self.a}x + {self.b} mod {self.p}"

    def __repr__(self):
        return str(self)
    
    def plot(self):
        points = self.points
        tuples = [(point.x, point.y) for point in points]
        x, y = zip(*tuples)
        fig, ax = plt.subplots(figsize=(6, 6), dpi=100)
        ax.scatter(x, y)
        ax.grid(True)
        plt.show()