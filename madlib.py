# This program requests words from the user
# and uses them to produce a Madlib

# Welcome the user
print("Welcome to Matt's Mablibs!")
print("To begin we need to collect some words.")
print("Please enter the appropriate word(s) according to the prompts below.")
print("Thanks for playing!")

# get some words
noun1 = input("Please enter a singular noun:")
verb1 = input("Please enter a past tense verb:")
adj1 = input("Please enter an adjective:")
noun2 = input("Please enter plural noun:")
noun3 = input("Please enter a singular noun:")
noun4 = input("Please enter another singular noun:")
num1 = input("Please enter a number:")
noun5 = input("Please enter plural noun:")
place1 = input("Please a place:")
drink = input("Please enter the name of a liquid:")
place2 = input("Please a place:")
noun6 = input("Please enter a singular noun:")
adj2 = input("Please enter an adjective:")
verb2 = input("Please enter a past tense verb:")

# Give the output
print("")
print("Today I went to the beach. I saw a " + noun1 + " splashing in the waves.")
print("It " + verb1 + " into the deeper water to catch some " + adj1 + " " + noun2 + ". I was amazed!")
print("As I stood watching, a " + noun3 + " flew down to the beach and landed on a " + noun4 + ".")
print("It was soon joined by " + num1 + " of its " + noun5 + ". As much as I enjoyed this I soon became thirsty and hot.") 
print("I walked back to the " + place1 + " to get a refreshing glass of " + drink + " to drink.")
print("Then I made my way back to the " + place2 + " so I could make a " + noun6 + " of all the " + adj2 + " things I had " + verb2 +" that day.")

# End of output, thank the user
print("")
print("")
print("Thank you for visiting Matt's Madlibs!")
print("Have a great day and come back soon for more Madlibs!")
