from stats import number_of_words, letter_counter

def get_book_text():

    with open('books/frankenstein.txt') as f:
        return f.read()



number_of_words(get_book_text())
letters = letter_counter(get_book_text())
print(letters)