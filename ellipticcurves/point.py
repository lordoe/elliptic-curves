from .utils import multiplicative_inverse

class Point:
    def __init__(self, x, y, curve):
        if x != None and y != None and y**2 % curve.p != (x**3 + curve.a*x + curve.b) % curve.p:
            raise ValueError('Point is not on curve')
        self.curve = curve
        self.x = x
        self.y = y

    def __add__(self, other):
        if self.curve != other.curve:
            raise TypeError('Points are not on the same curve')
        if self.x is None and self.y is None:
            return other
        if other.x is None and other.y is None:
            return self
        if self.x == other.x and self.y == self.curve.p - other.y:
            return Point(None, None, self.curve)
        if self.x == other.x and self.y == other.y:
            return self.double()
        denom = multiplicative_inverse(other.x - self.x, self.curve.p)
        s = (other.y - self.y) * denom % self.curve.p
        x3 = (s**2 - self.x - other.x) % self.curve.p
        y3 = (s*(self.x - x3) - self.y) % self.curve.p
        return Point(x3, y3, self.curve)
    
    def __mul__(self, other):
        if not isinstance(other, int):
            raise TypeError('Multiplication is only defined for integers')
        if other < 0:
            raise ValueError('Multiplication is not implemented for negative integers')
        result = Point(None, None, self.curve)
        addend = self
        while other:
            if other & 1:
                result += addend
            addend += addend
            other >>= 1
        return result
    
    def double(self):
        denom = multiplicative_inverse(2*self.y, self.curve.p)
        s = (3*self.x**2 + self.curve.a) * denom % self.curve.p
        x3 = (s**2 - 2*self.x) % self.curve.p
        y3 = (s*(self.x - x3) - self.y) % self.curve.p
        return Point(x3, y3, self.curve)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return str(self)