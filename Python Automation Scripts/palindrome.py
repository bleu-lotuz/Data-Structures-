class palindrome:
    def palindrome(number : int):
        reverse = 0
        temp = number
        while temp > 0:
            remainder = temp % 10
            reverse = (reverse * 10) + remainder
            temp = temp // 10
        if number == reverse:
            return "Is a Palindrome"
        else:
            return "Not a Palindrome"


if __name__ == "__main__":
    import doctest

    doctest.testmod()

    number = float(input("Enter the number to check if it is a palindrome"))
    print(palindrome.palindrome(number))
