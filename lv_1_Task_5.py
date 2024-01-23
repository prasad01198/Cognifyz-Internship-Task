def palindrome(word):
    # defining a empty string to store reversed word
    rev = ''

    # reversing a inputted word
    for char in word:
        rev = char + rev
    
    # checking if reversed and original string is same if yes then palindrome or not
    if rev == word:
        print(f"{word} is palindrome")
    else :
        print(f"{word} is not palindrome")

if __name__ == '__main__':    
    while True:
        # Taking a string input from a user
        word = input("Enter a word: ")

        # Calling a function
        palindrome(word)
    
        # asking user to continue or not
        cont = input("Do you wanna try another word? Y/N : ")
        cont = cont.upper()
        if cont !='Y':
            print("Thank you! ")
            break