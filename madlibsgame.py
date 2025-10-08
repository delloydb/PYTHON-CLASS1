# madlibs game
# word game where we create a story template with blanks for words
# by filling in the blanks we create a funny story

adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
adjective3 = input("Enter one more adjective: ")

noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")

verb1 = input("Enter a verb: ")
verb2 = input("Enter another verb: ")

print("Here is your story: ")
print("Once upon a time, there was a " + adjective1 + " " + noun1 + ".")
print("Every day, it would " + verb1 + " with a " + adjective2 + " " + noun2 + ".")
print(
    "One day, they decided to " + verb2 + " to a " + adjective3 + " adventure together."
)
print("And they lived happily ever after!")
# Example inputs:
# adjective1: funny
# adjective2: blue
# adjective3: exciting
# noun1: cat
# noun2: dog
# verb1: play
# verb2: go on

# Example output:
# Here is your story:
# Once upon a time, there was a funny cat.
# Every day, it would play with a blue dog.
# One day, they decided to go on to a exciting adventure together.
# And they lived happily ever after!
