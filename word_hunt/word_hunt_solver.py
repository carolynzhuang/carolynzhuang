import random
import string
import os

# Creating a list of all possible words given a dictionary
with open(os.path.expanduser("/Users/carolynzhuang/Desktop/Berkeley/CSK/Collins_Dictionary.txt"),"r") as collins_dictionary:
    dictionary = [line.strip() for line in collins_dictionary]

# Generating a random map given the dimensions of a map
def generate_map(width, height):
    letters = list(string.ascii_uppercase) 
    generated_map = [] 
    for i in range(height):
        row = []
        for j in range(width):
            row.append(random.choice(letters))
        generated_map.append(row)
    return generated_map

generated_map = generate_map(4,4) 
print(generated_map)
generated_letters = "".join([ele for sub in generated_map for ele in sub]) #Converting the matrix into a string

# Example map from Word Hunt
# example_letters = "OANGHIEDKHTRCSAL"
# example_map = [list(example_letters[i:i+4]) for i in range(0, len(example_letters), 4)]

# Choosing a map
input_map = generated_map
input_letters = generated_letters
# input_map = example_map
# input_letters = example_letters

# Creating a dictionary where each letter on the map is assigned a key, which gives the positions where the letter appears on the map
letters = {} 
for i in range(len(input_letters)):
    if input_letters[i] in letters.keys():
        letters[input_letters[i]].append(i+1)
    else:
        letters[input_letters[i]] = [i+1]

# All possible movements (neighboring positions) from a given position in the map
# id_mappings = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]] Assigns each position a number
id_movements = {
    1: [2,5,6],
    2: [1,3,5,6,7],
    3: [2,4,6,7,8],
    4: [3,7,8],
    5: [1,2,6,9,10],
    6: [1,2,3,5,7,9,10,11],
    7: [2, 3, 4, 6, 8, 10, 11, 12],
    8: [3, 4, 7, 11, 12],
    9: [5, 6, 10, 13, 14],
    10: [5, 6, 7, 9, 11, 13, 14, 15],
    11: [6, 7, 8, 10, 12, 14, 15, 16],
    12: [7, 8, 11, 15, 16],
    13: [9, 10, 14],
    14: [9, 10, 11, 13, 15],
    15: [10, 11, 12, 14, 16],
    16: [11, 12, 15],
}

# Mapping the position of the letters on the map
ids_to_letters = {
    1: input_map[0][0],
    2: input_map[0][1],
    3: input_map[0][2],
    4: input_map[0][3],
    5: input_map[1][0],
    6: input_map[1][1],
    7: input_map[1][2],
    8: input_map[1][3],
    9: input_map[2][0],
    10: input_map[2][1],
    11: input_map[2][2],
    12: input_map[2][3],
    13: input_map[3][0],
    14: input_map[3][1],
    15: input_map[3][2],
    16: input_map[3][3],
}

# Finding the adjacent locations available for the next letter
def find_word(letter, current_word):
    if len(current_word) == 0: # No letters in the word (finding the first placement)
        if letter in letters.keys():
            return letters[letter] 
    else:
        if letter in letters.keys(): # The word has already been started
            positions = []
            for location in letters[letter]:
                if location in id_movements[current_word[-1]] and location not in current_word: # Checks that the new position is possible given the last position of the current word and that the new position has not already been used
                    positions.append(location)
            return positions 
    return []

# Depth-First Search algorithm to check whether a word can be formed on the map
def check_letters(letters, already_used):
    if len(letters) == 0: 
        return True
    options = find_word(letters[0], already_used) # Uses the find_word function to find possible starting positions
    if options:
        for option in options:
            if check_letters(letters[1:], already_used + [option]): # Extracts remaining letters of the word, combines positions that have already been used, recursively calls check_letters
                return True 
    return False 

# Finding all solutions to a map
def solve_map(dictionary):
    words_found = [] 
    for word in dictionary: 
        if len(word) < 3: 
            continue
        options = check_letters(word, []) 
        if options: 
            words_found.append(word) 
    return words_found

# Printing the results
solutions = sorted(solve_map(dictionary), key = len, reverse = True) 
output_solutions = '\n'.join(solutions) 
print(len(solutions), "words found:") 
print(output_solutions)