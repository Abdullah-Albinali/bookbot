def number_of_words(book):
    num_words =  len(book.split())
    print(f"{num_words} words found in the document")

def letter_counter(book):
    letters = {}
    for word in book.split():
        for  letter in word:
            if str.lower(letter) not in letters:
                letters[str.lower(letter)] = 1
            else:
                letters[str.lower(letter)] += 1

    return letters

