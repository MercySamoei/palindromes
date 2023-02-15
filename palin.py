def is_palindrome(text):
    return text == text[::-1]

with open('words_in_english_dictionary.txt', 'r') as file:
    text = file.read()

words = text.split()

palindromes = []
for word in words:
    if is_palindrome(word):
        palindromes.append(word)

if palindromes:
    for palindrome in palindromes:
        print(palindrome)






