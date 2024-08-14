import pandas

# reading dataframe
df = pandas.read_csv("nato_phonetic_alphabet.csv")

# # creating lists out of dataframe
# letters = []
# codes = []
# for (key, value) in df.iterrows():
#     letters.append(value.letter)
#     codes.append(value.code)
#
# # using dictionary comprehension to convert dataframe into dictionary
# data = {key: value for (key, value) in zip(letters, codes)}

# OR

data = {value.letter: value.code for (index, value) in df.iterrows()}

# getting user input
input_word = input("Enter a word: ").upper()
output = []
for letter in input_word:
    # creating a list of words using dictionary
    output.append(data[letter])

print(output)
