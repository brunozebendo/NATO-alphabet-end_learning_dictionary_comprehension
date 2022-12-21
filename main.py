'''o objetivo do código é criar um dicionário que vai pegar cada letra da palavra inserida e relacionar
com a palavra utilizada no código fonético da OTAN, para isso, primeiro, a variável data recebe
 o arquivo csv que é lido através do método pandas.read_csv, depois é criado um dicionário {} através do
 método interrows que itera pelo arquivo CSV e relaciona a primeira coluna (letter) como key e a segunda  coluna (code)
  como o value, assim é criado o dicionário {'A': 'Alfa', 'B': 'Bravo', 'C': 'Charlie', 'D': 'Delta',
  ... e por aí vai. Já o segundo código pega a palavra digitada pelo usuário guarda na variável word, então
  pega a key letter no phonetic_dict e imprime o seu valor. Reparar como aqui se usou [] para acessar o valor  da key
   no dicionário'''


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
#TODO 1. Create a dictionary in this format:
phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}
print(phonetic_dict)

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

word = input("Enter a word: ").upper()
output_list = [phonetic_dict[letter] for letter in word]
print(output_list)
