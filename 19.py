# How Do You Handle Exceptions With Try/Except/Finally In Python?
# Explain with coding snippets. 

try:
    number=int(input("Enter a numberc:- "))
    result=10/number
    print(result)
except ValueError:
    print("Error: Invalid input Please enter a valid number.")
finally:
    print("Execution complete.")