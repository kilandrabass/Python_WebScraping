import requests


def count_occurrences_in_year(names, year):
  webpage = f"https://en.wikipedia.org/wiki/{year}th_Academy_Awards" #Wiki URL
  response = requests.get(webpage) #Fetch data from the webpage
  if response.status_code == 200:
    #Search for occurrences of the name in the page content
    content = response.text.lower() #Convert to lowercase for search
    #Count occurrences for each name
    occurrences = [content.count(name.lower()) for name in names]
    #Check if any name has occurrences greater than 0
    if any(occurrences):
        # Print results only if at least one name appears
        print(f"\nResults for the {year}th Oscars:")
        for name, count in zip(names, occurrences):
            print(f"{name} appears {count} times")
    
def main():
  #Enter first actors name (ie:Denzel Washington)
  name1 = input("Enter an actor's name: ") 
  #Enter second actors name (ie:Meryl Streep)
  name2 = input("Enter another actor's name: ") 
  for year in range(1, 94): #Iterate through the Academy Awards years
    #Call function to count occurrences of entered names in the webpage of each year
    count_occurrences_in_year([name1, name2], year)
      
if __name__ == "__main__":
  main()