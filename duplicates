#Count the Number of Duplicate Characters
#Create a function that returns the amount of duplicate characters in a string. It will be case sensitive and spaces are included. If there are no duplicates, return 0.
#link to task https://edabit.com/challenge/mgBdGGw7StxF2tBqu

def duplicates(txt):
    letter_dict = {}
    for l in txt:
        letter_dict[l] = letter_dict.get(l,0) + 1
    count = 0
    for value in letter_dict.values():
        count += value
    return count - len(letter_dict)
