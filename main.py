import pandas

Nato_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
Nato_Dict = {row.letter : row.code for (index,row) in Nato_alphabets.iterrows()}

def generate_nato():
    User_Input = input("Enter the word : ").upper()
    try:
        Nato_Code = [Nato_Dict[letter] for letter in User_Input]
    except KeyError:
        print("Enter alphabets only")
        generate_nato()
    else:
        
        print(Nato_Code)

generate_nato()