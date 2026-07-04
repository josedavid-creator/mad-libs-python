#Creativity: I added a friendly message before displaying the story to make the program more interactive and encourage the user to choose creative words.

"""
Author: Jose Vera

Purpose: This program asks the user for different words and creates a funny Mad Libs story using their answers.
"""

print("Please enter the following:")
print()
adjective = input(f"adjective:")

animal = input(f"animal:")

verb = input(f"verb:")

exclamation = input(f"exclamation:")

verb1 = input(f"verb:")

verb2 = input(f"verb:") 
print()

print("I hope you chose your answers carefully; this will make the story much more fun.")
print()

print("Your story is:")
print()
print(f"The other day, I was really in trouble. It all started when I saw a very")
print(f"{adjective.lower()} {animal.lower()} {verb.lower()} down the hallway. \"{exclamation.capitalize()}!\" I yelled. But all")
print(f"I could think to do was to {verb1.lower()} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb2.lower()}")
print(f"right in front of my family.")