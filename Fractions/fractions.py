class Fraction:
  
  def __init__(self, numerator, denominator):

    self.numerator = numerator
    self.denominator = denominator

  def __str__(self):

    return str(self.numerator) + "/" + str(self.denominator)

a = Fraction(1,2)
print(a)