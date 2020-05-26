vowels = ['a', 'e', 'i', 'o', 'u']
def pigLatin(word):
    letters = list(word)

    index = 0
    vowel = False
    while vowel == False:
        for letter in vowels:
            if letters[index] == letter:
                vowel = True
        index += 1
    if index == 1:
        print(word + 'way')
    else:
        first_part = ''.join([elem for elem in letters[0:index-1]])
        rest_of_word = ''.join([elem for elem in letters[index-1:]])
        print(rest_of_word + first_part + 'ay')
pigLatin('algorithm')