class ComplexNum:
    def __init__(self, real, imgn):
        self.real = real
        self.imgn = imgn

    def __add__(self, other):
        return ComplexNum(self.real + other.real, self.imgn + other.imgn)

    def __mul__(self, other):
        return ComplexNum(self.real * other.real - self.imgn * other.imgn,
                          self.imgn * other.real + self.real * other.imgn)

    def __str__(self):
        if self.real == 0:
            if self.imgn != 0:
                return f'{self.imgn}j'
            elif self.imgn == 0:
                return '0'
        else:
            if self.imgn > 0:
                return f'{self.real} + {self.imgn}j'
            elif self.imgn == 0:
                return f'{self.real}'
            else:
                return f'{self.real} {self.imgn}j'


a = ComplexNum(0, 1)
b = ComplexNum(2, 0)
f = ComplexNum(5, -12)
k = ComplexNum(-5, -6)
print(f'{a},\n{b},\n{f},\n{k}')
print(a + b)
print(a * k)
print(f + k)
