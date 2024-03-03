# Chris Oesterling 11/20/22 ISIT333

# first import pandas
import pandas as pd

# then save data to a variable "pokemon"
pokemon = pd.read_csv("pokemon.csv")


def example():
  ## EXAMPLE DATA CALLS - COMMENT OR REMOVE lines 7 - 25 BEFORE SUBMITTING
  
  # print first 5 records
  print()
  print("Top 5 records\n")
  print(pokemon.head(5))
  
  # print information about csv data
  print()
  print("Basic information about the Pokemon data\n")
  print(pokemon.info())
  
  # print statistical information about all records in the data file
  print()
  print("Basic statistical information about the Pokemon data\n")
  print(pokemon.describe())
  
  # print information about the number of unique values in each column 
  print()
  print("Information about the number of unique values in each column\n")
  print(pokemon.nunique())
  
  
  # print the minimum value of HP column - note this should align with the data in the describe() function
  print("The minimum HP value is", pokemon["HP"].min())


# 1 - Print out a report with only the following fields displaying - Name, Type, Generation
def one():
  print("\nName, type and generation\n")
  print(pokemon[["Name", "Type 1", "Type 2", "Generation"]])
  #print(pokemon[])


# 2 - Print out a report displaying the name, HP, Attack, Defense, Speed 
def two():
  print("\nName, HP, Attack, Defense, Speed\n")
  print(pokemon[["Name", "HP", "Attack", "Defense", "Speed"]])

# 3 - Create a dataFrame displaying all of the GRASS type Pokemon in the csv file
def three():
  print("\nGrass type pokemon\n")
  
  pokemon[pokemon["Type"] == "grass"]
  #grass = pokemon["Type 1"] == "Grass"
  #print(pokemon[grass])

# 4 - Create a dataFrame displaying all of the Pokemon in order of HP (highest to lowest)
def four():
  print("\nHP from highest to lowest\n")
  print(pokemon.sort_values(["HP"], ascending=[False]))

# 5 - Create a dataFrame displaying all of the Pokemon in order of NAME A-Z
def five():
  print("\nPokemon in order of name\n")
  print(pokemon.sort_values(["Name"], ascending=[True]))

# 6 - Create a dataFrame of all the LEGENDARY Pokemon. 
def six():
  print("\nAll Legendary pokemon\n")
  print(pokemon[pokemon["Legendary"] == True])

# 7 - Create a search for a name of a Pokemon and return the data associated with the Pokemon. Do a try/except to catch any error or record not found. Allow the user to search multiple times until they choose to exit.
def seven():
  while True:
    
    try:
      name = input("\nPlease enter the name of a pokemon you would like to search for: ")
      poke = pokemon[pokemon['Name'] == name]
      if (poke.empty == True):
        print("\nSorry, pokemon not found")
      else:
        print(poke)
      
    except:
      print("e")
  
    again = input("\nWould you like to search again? Y/N ")
    if again.upper() == "N":
      break


def menu():
  print("\nPlease select one of the options below:")
  print("1: Name, Type and Generation")
  print("2: Name, HP, Attack, Defense, Speed")
  print("3: Grass type pokemon")
  print("4: All pokemon from highest HP to lowest")
  print("5: List pokemon in alphabetical order")
  print("6: List all legendary pokemon")
  print("7: Look up a pokemon")
  print("8: exit program")

def main():
  print("Welcome to the Pokedex!")

  #While menu Loop
  while True:
    menu()
    A = int(input())
    if A == 1:
      one()
    elif A == 2:
      two()
    elif A == 3:
      three()
    elif A == 4:
      four()
    elif A == 5:
      five()
    elif A == 6:
      six()
    elif A == 7:
      seven()
    elif A == 8:
      break
    else:
      print("\nSorry, please select a number on the menu")

  print("\nThanks for using the Pokedex")

if __name__ == "__main__":
  main()