
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def main():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
 

    choice = input("Enter choice (1/2/): ")

  
    if choice in ('1', '2',):
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            print(f"{num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1, num2)}")
      
    else:
        print("Invalid input! Please choose a valid operation.")


