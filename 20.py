# Write python program that user to enter only odd numbers, else will raise an exception. 


while True:
    try:
        number = int(input("Please enter an odd number :- "))
        if number % 2 == 0:
            raise ValueError("number is not odd. Please enter an odd number.")
        print("odd number :-",number)
        break
    except ValueError as e:
        print(e)
    except Exception:
        print("Invalid input enter a valid number.")
