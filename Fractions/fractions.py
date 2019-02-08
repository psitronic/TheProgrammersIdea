class Fraction:
  
  def __init__(self, numerator, denominator):

    self.numerator = numerator
    self.denominator = denominator

  def __add__(self, other):

    new_denominator = self.denominator * other.denominator

    new_numerator = self.numerator * other.denominator + other.numerator * self.denominator

    return Fraction(new_numerator, new_denominator)

  def __gt__(self, other):

    return self.numerator * other.denominator > other.numerator * self.denominator

  def __lt__(self, other):

    return self.numerator * other.denominator < other.numerator * self.denominator

  def __eq__(self, other):

    return self.numerator * other.denominator == other.numerator * self.denominator

  def __str__(self):

    return str(self.numerator) + "/" + str(self.denominator)

a = Fraction(2,4)
b = Fraction(1,2)

print(a == b)