for n in range(1,101):
    if n%3==0:
        if n%15==0:
            print("FizzBuzz")
        else:
            print("Fizz")
    elif n%5==0:
        if n%15==0:
            print("FizzBuzz")
        else:
            print("Buzz")
    else:
        print(n)