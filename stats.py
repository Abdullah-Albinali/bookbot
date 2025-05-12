def number_of_words(book):
    num_words =  len(book.split())
    return(f"Found {num_words} total words")


def letter_counter(book):
    letters = {}
    for word in book.split():
        for  letter in word:
            if str.lower(letter) not in letters:
                letters[str.lower(letter)] = 1
            else:
                letters[str.lower(letter)] += 1

    return letters

def sort_letters_by_count(letters):

    ordered_letters_by_count = list(letters.values())
    ordered_letters_by_count.sort(reverse=True)

    exersie_request = []
    for item in ordered_letters_by_count:
        exersie_request.append({"char":list(letters.keys())[list(letters.values()).index(item)],"num":item})

    return exersie_request

