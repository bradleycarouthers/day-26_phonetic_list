import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}


def generate_phonetic():
    choice = input("Type a word or words: ").upper()
    new_choice = choice.replace(" ", "")
    try:
        choice_list = [phonetic_dict[letter] for letter in new_choice]
    except KeyError:
        print("Sorry, only letters in the alphabet please")
        generate_phonetic()
    else:
        print(choice_list)


generate_phonetic()
