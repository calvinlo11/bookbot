from stats import num_of_words
from stats import count_characters

def get_book_text(file_path):
    try:
        with open(file_path, 'r') as file:
            contents = file.read()
            return contents
    except FileNotFoundError:
        print("The file does not exist.")
    except Exception as e:
        print(f"And error occurred: {e}")


def main():
    book_text = get_book_text("../bookbot/books/frankenstein.txt")
    print(num_of_words(book_text))
    print(count_characters(book_text))
if __name__ == "__main__":
    main()