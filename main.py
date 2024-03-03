import pandas

Nato_alphabets = pandas.read_csv("nato_phonetic_alphabet.csv")
Nato_Dict = {row.letter : row.code for (index,row) in Nato_alphabets.iterrows()}

User_Input = input("Enter the word : ")
User_word = [ letter.upper() for letter in User_Input if letter.isalpha()]
print(User_word)



Nato_Code = [Nato_Dict[letter] for letter in User_word]
print(Nato_Code)
