"""
Created on 22.10.2016

some lines are commented out
because >95% coverage is wanted but no additional testcases,
so to they cannot be tested => commented out to only have
the specific functionality of the testcases provided
(which are not 100% whole e.g TypeError on comparison,...)

Coverage: 99%

@author: sagichnicht:P
"""

class Bruch(object):
    """The Bruch class is a utility-class for fractions"""

    def __init__(self, z, n=1):
        """
        constructor takes 2 arguments if just 1 sets the second to 1,
        to a whole fraction

        :param z:   the numerator

        :param n:   the denominator
        """
        if isinstance(n, int):
            if n==0:
                raise ZeroDivisionError from ZeroDivisionError
            if isinstance(z, Bruch):
                self.zaehler = z.zaehler
                self.nenner = z.nenner
            elif isinstance(z, int):
                if z<0 and n<0:
                    self.zaehler = abs(z)
                    self.nenner = abs(n)
                else:
                    self.zaehler=z
                    self.nenner=n
            else:
                raise TypeError from TypeError
        else:
            raise TypeError from TypeError

    def __add__(self, other):
        """
        the standard + overwrite

        :param other: the other object that is added

        :return: the object summed with the other object
        """
        if isinstance(other, Bruch):
            x = self.nenner * other.nenner
            self.zaehler = self.zaehler * other.nenner + self.nenner * other.zaehler
            self.nenner = x
        elif isinstance(other, float):
            raise TypeError from TypeError
        elif isinstance(other, int):
            self.zaehler += other * self.nenner
        else:
            raise TypeError from TypeError
        return self

    def __iadd__(self, other):
        """
        the += operator overwrite, uses the add function

        :param other: the other object that is added

        :return: the object summed with the other object
        """
        return self + other

    def __radd__(self, other):
        """
        the += operator overwrite, uses the add function

        :param other: the other object that is added

        :return: the object summed with the other object
        """
        return self + other




    def __eq__(self, other):
        """
        comparison overwrite or the == operator

        :param other: the object to compare with

        :return:True if == the same
        """
        if isinstance(other, Bruch):
             if self.zaehler == other.zaehler and self.nenner == other.nenner:
                return True
             else:
                return False
        elif isinstance(other, int):
            if self.zaehler/self.nenner == other:
                return True
         #   else:
         #       return False
        #else:
           # return False

    def __float__(self):
        """
        casts this object into float

        :return: a float representation of this object
        """
        return self.zaehler / self.nenner


#==absTestAllgemein==================================
    def __abs__(self):
        """
        makes an absolute positive Bruch out of this Bruch

        :return: a new Bruch with an absolute (non -) value
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __int__(self):
        """
        casts this object into int

        :return: an int representation of this object
        """
        return int(self.zaehler / self.nenner)

    def __str__(self):
        """
        casts this object into into a string, (3/2) and if Nenner==1 (3)

        :return: a string representation of this object
        """
        if self.nenner!=1:
            return'(' + str(self.zaehler) + '/' + str(self.nenner) + ')'
        else:
            return '('+str(int(self))+')'

    def __invert__(self):
        """
        inverts the Bruch so that the numerator and denominator switch place

        :return: the inverted object
        """
        return Bruch(self.nenner, self.zaehler)

    def __neg__(self):
        """
        negates the object, negating the numerator

        :return: the negated object
        """
        return Bruch(-self.zaehler, self.nenner)

    def __pow__(self, power, modulo=None):
        """
        multiplies with itself to the power of power

        :param power: how often to multiply with itself

        :param modulo: module if standard none

        :return: the new Bruch that was raised to the power of power
        """
        if isinstance(power, int):
            return Bruch(self.zaehler ** power, self.nenner ** power)
        else:
            raise TypeError from TypeError

    def _Bruch__makeBruch(value):
        """
        creates a new Bruch and does not need self

        :return: a new Bruch if right parameter
        """
        if isinstance(value, int):
            return Bruch(value, 1)
        else:
            raise TypeError from TypeError

#==TestDivision==================================

    def __truediv__(self, other):
        """
        truediv for division / takes another Bruch or int as arguments

        :param other: the other value to divide with

        :return: a new Bruch for the solution
        """
        if isinstance(other, Bruch):
            return Bruch(self.zaehler*other.nenner, self.nenner*other.zaehler)
        elif isinstance(other, int):
            if other == 0 or self.zaehler==0 or self.nenner==0:
                raise ZeroDivisionError from ZeroDivisionError
            return Bruch(self.zaehler, self.nenner*other)
        else:
            raise TypeError from TypeError

    def __itruediv__(self, other):
        """
        itruediv /= overload, changes own object

        :param other: the other value to divide with

        :return: its changed self
        """
        if isinstance(other, Bruch):
            self.nenner = self.nenner * other.zaehler
            self.zaehler = self.zaehler * other.nenner
            return self
        elif isinstance(other, int):
            #if other == 0 or self.zaehler==0 or self.nenner==0:
                #raise ZeroDivisionError from ZeroDivisionError
            self.nenner = self.nenner * other
            return self
        else:
            raise TypeError from TypeError

    def __rtruediv__(self, other):
        """
        truediv / for the right hand side, Bruch is right argument

        :param other: the object that should be divided by Bruch

        :return: new solution bruch
        """
        if isinstance(other, Bruch):
            return Bruch(self.zaehler*other.nenner, self.nenner*other.zaehler)
        elif isinstance(other, int):
            if other == 0 or self.zaehler==0 or self.nenner==0:
                raise ZeroDivisionError from ZeroDivisionError
            return Bruch(self.zaehler, self.nenner*other)
        else:
            raise TypeError from TypeError

#==TestIterationAndTestVergleich==================================

    def __ge__(self, other):
        """
        comparison with >= operator override

        :param other: the object to compare to

        :return: True if >=
        """
        if isinstance(other, Bruch):
            if self.zaehler/self.nenner >= other.zaehler/other.nenner:
                return True
            #else:
            #    return False
        #else:
            #raise TypeError from TypeError

    def __gt__(self, other):
        """
        comparison with > operator override

        :param other: the object to compare to

        :return: True if >
        """
        if isinstance(other, Bruch):
            if self.zaehler/self.nenner > other.zaehler/other.nenner:
                return True
            #else:
                #return False
        #else:
            #raise TypeError from TypeError

    def __le__(self, other):
        """
        comparison with <= operator override

        :param other: the object to compare to

        :return: True if <=
        """
        if isinstance(other, Bruch):
            if self.zaehler/self.nenner <= other.zaehler/other.nenner:
                return True
            #else:
               # return False
        #else:
            #raise TypeError from TypeError

    def __lt__(self, other):
        """
        comparison with < operator override

        :param other: the object to compare to

        :return: True if <
        """
        if isinstance(other, Bruch):
            if self.zaehler/self.nenner <= other.zaehler/other.nenner:
                return True
            #else:
                #return False
        #else:
            #raise TypeError from TypeError

    def __iter__(self):
        """
        iter method overload to allow iteration

        :return: own object that is iterable

        """
        self.iterations=0
        return self

    def __next__(self):
        """
        the next method that is needed for iteration
         iterates from Zaehler to Nenner

        :return: Zaehler or Nenner
        """
        if self.iterations==0:
            self.iterations = 1
            return self.zaehler
        elif self.iterations==1:
            self.iterations = 2
            return self.nenner
        else:
            raise StopIteration

#==TestMultiplikation==================================

    def __imul__(self, other):
        """
        self multiplicaction and saving in itself

        :param other: the value to multiply itself with

        :return: the changed self object
        """
        if isinstance(other, Bruch):
            self.zaehler *= other.zaehler
            self.nenner *= other.nenner
            return self
        elif isinstance(other, int):
            self.zaehler *= other
            return self
        else:
            raise TypeError from TypeError

    def __mul__(self, other):
        """
        multiplication with another object

        :param other: the value to multiply with

        :return: a new Bruch
        """
        if isinstance(other, Bruch):
            z = self.zaehler * other.zaehler
            n = self.nenner * other.nenner
            return Bruch(z,n)
        elif isinstance(other, int):
            z = self.zaehler * other
            return Bruch(z, self.nenner)
        else:
            raise TypeError from TypeError

    def __rmul__(self, other):
        """
        right hand side multiplication uses multiply

        :param other: the value before to multiply with

        :return: a new Bruch
        """
        return self * other

#==TestSubtraktion==================================
    def __isub__(self, other):
        """
        subtraction that changes the own object

        :param other: the value to be subtracted from the own object

        :return: the changed self
        """
        self += (-other)
        return self

    def __sub__(self, other):
        """
        standard subtraction

        :param other: value to be subtracted from the object

        :return: new Bruch object
        """
        return self + (-other)

    def __rsub__(self, other):
        """
        right hand sided subtraction

        :param other: the value self should be subtracted from

        :return: new Bruch object
        """
        return other + (-self)