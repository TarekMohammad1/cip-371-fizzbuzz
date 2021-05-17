""" FizzBuzz!

Prints the Fizz Buzz sequence up to a given number.

Authored by: Section 371 of Code in Place
Contributors:
* Jay
* Tarek
"""

def main():
    # ask the user for input, as a string
    user_number_str = input("Enter a number to count to: ")

    # transform the string into an integer
    user_number = int(user_number_str)

    # repeat the indented code below as many times as the user number
    for i in range(1, user_number+1):
        
        # check whether the current number is divisible by both 10 and 15
        if i % 10 == 0 and i % 15 == 0:
            print("fizzbuzz")
        # check whether the current number is divisible by 10
        elif i % 10 == 0: 
            print("fizz")
        # check whether the current number is divisible by 15
        elif i % 15 == 0:
            print("buzz")
        else:
            print(i)

 
if __name__ == '__main__':
    main()
