# function to convert temperature from fahrenheit to celsius
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

# function to convert temperature from celsius to fahrenheit 
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

if __name__ == "__main__":
    while True:
        # taking input from user
        choice = int(input("What do you want to do?\n 1. fahrenheit to celsius \n 2. celsius to fahrenheit \n"))
        
        # base on input calling a function
        if choice ==1:
            temperature = float(input("Enter temperature  in fahrenheit: "))
            print(f"converted {temperature} from fahrenheit to celsius result is:{fahrenheit_to_celsius(temperature)}")
        elif choice ==2:
            temperature = float(input("Enter temperature  in celsius: "))
            print(f"converted {temperature} from celsius to fahrenheit result is:{celsius_to_fahrenheit(temperature)}")
        else:
            print("Ohooo! You have entered a invalid input. ")
    
        cont = input("Do you wish to continue with another operation? y/n :")
        cont = cont.upper()
        
        if cont != 'Y':
            print("Thank you !")
            break