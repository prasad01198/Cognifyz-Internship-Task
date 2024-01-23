import re

def count_occurrence(path):
    count_of_words = {}

    # Opening a file in read mode to read its content
    with open(path, 'r') as file:
        content = file.read()
        print(f"\nThe file contain\n\n{content}")

        # using RegEx to extract words
        words = re.findall(r'\b\w+\b', content)

        # counting occurrence of each word
        for word in words:
            word = word.lower()  
            count_of_words[word] = count_of_words.get(word, 0) + 1

    return count_of_words

def count_words(count_of_words):
    # Displaying result in alphabetical order
    sorted_words = sorted(count_of_words.keys())
    for word in sorted_words:
        print(f'{word} : {count_of_words[word]}')

if __name__ == "__main__":
    # defining path to the file
    path = 'D:\Programs\Python\Cognifyz\Book1.csv'

    # Counting word occurrences
    count_of_words = count_occurrence(path)

    # Displaying results
    count_words(count_of_words)