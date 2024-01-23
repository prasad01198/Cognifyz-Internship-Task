import random

def Guessing_game():
    # Running a loop to let the user play again    
    while True:

        # generating random number
        random_number = random.randint(1,100)
        # print(random_number)
        
        #Asking user to input a number 
        num=int(input("choose an integer from 1 to 100 : "))
        
        # comparing the inputted number
        if num == random_number:
            print("Congratulation you guess the right number")
            
        elif num > random_number:
            print("Off oh! Your guessing is higher than the number... ")
            
        else :
            print("Off oh! Your guessing is lower than the number... ")
        
        # Asking user to continue or not
        cont = input("Do you want to continue press Y or press any key : ")
        cont = cont.upper()
        if cont != 'Y':
            print("Thank you for participation! ")
            break
            
if __name__ == "__main__":
    Guessing_game()