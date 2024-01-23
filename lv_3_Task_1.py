import requests
from bs4 import BeautifulSoup

def headlines(website):
    try:
        # Sending an HTTP request to the specified website
        response = requests.get(website)
        response.raise_for_status()

        # Parsing the HTML content of the page using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Defining scraping logic for each website
        if 'indiatimes' in website:
            headlines = soup.find_all(class_='card-title')
        elif 'lokmat' in website:
            headlines = soup.find_all(['h2'])
        else:
            print("Unsupported website.")
            return

        # Displaying the headlines
        if headlines:
            for index, headline in enumerate(headlines, start=1):
                title = headline.text.strip()
                print(f"{index}. {title}")
        else:
            print("No headlines found on the specified website.")

    except requests.exceptions.RequestException as e:
        print(f"Error: Unable to fetch data from the website. {e}")

if __name__ == "__main__":
    
    # taking the input from the user to display particular headlines
    choose = int(input("Which headlines do you like to watch today?\n1. India Times\n2. Lokmat\n"))

    if choose == 1:
        website = 'https://www.indiatimes.com/news/india'
    elif choose == 2:
        website = 'https://www.lokmat.com/maharashtra/'
    else:
        print("Invalid choice.")
        exit()

    headlines(website)