"""
This is a pure Python implementation of the Pythagoras Triplets algorithm
Run the doctests with the following command:
python3 -m doctest -v pythagoras_triplet.py
or
python -m doctest -v pythagoras_triplet.py
For manual testing run:
python3 pythagoras_triplet.py
"""


from math import sqrt
class pythagoras_triplet:
    def pythagoras(side1 : float, side2:  float) -> float:
        hypotenuse = sqrt(side1**2 + side2**2)
        return hypotenuse


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    side1 = float(input("Enter the side one of the right triangle"))
    side2 = float(input("Enter the side two of the right triangle"))

    print("Formula of hypotenuse  => sqare root of side1^2 + side2^2")
    print(pythagoras_triplet.pythagoras(side1, side2))
