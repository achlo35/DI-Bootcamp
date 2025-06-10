# Exercise 1: Currencies

class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def __str__(self):
        return f'{self.amount} {self.currency}'
    
    def __int__(self):
        return self.amount

    def __repr__(self):
        return f'{self.__class__.__name__} : {self.amount} {self.currency}'
    
    def __add__(self, other):
        if isinstance(other, Currency) and self.currency == other.currency:
            return Currency(self.currency, self.amount + other.amount)
        elif isinstance(other, int):
            return Currency(self.currency, self.amount + other)
        else:
            raise ValueError("Cannot add different currencies or non-Currency objects")
        

# Test the Currency class

c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

str(c1)

int(c1)

repr(c1)

print(c1 + 5)

print(c1 + c2) 

print(c1)

c1 += 5
print(c1)

c1 += c2
print(c1)

print(c1 + c3)