def calculator():
    try: 
        numa = float(input("Enter a :"))
        numb = float(input("Enter b :"))
        operation = input("Enter operation(+, -):")
        
        if operation == "+":
            results = numa + numb
        elif operation == "-":
            results = numa - numb
        else: 
            print("Invalid")
            return
        
        print(f"Results is: {results}")
    except ValueError: 
        print("invalid input")
if __name__ == "__main__":
    calculator()
        