from stats import number_of_words, letter_counter,sort_letters_by_count
import sys
def get_book_text(book):

    with open(book) as f:
        return f.read()

if len(sys.argv)<2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]
num_word = number_of_words(get_book_text(book))
letters = letter_counter(get_book_text(book))

temp = sort_letters_by_count(letters)

print("============ BOOKBOT ============")
print(f"Analyzing book found at {book}...")
print("----------- Word Count ----------")
print(num_word)
print("--------- Character Count -------")
for item in temp:
    if str.isalpha(item["char"]):
        print(f"{item["char"]}: {item["num"]}")

