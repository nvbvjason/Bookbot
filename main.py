def get_book_text(filepath):
    with open(filepath, 'r') as file:
        return file.read()

def main():
    text = get_book_text("books/frankenstein.txt")
    num_words = len(text.split())
    print(f"{num_words} words found in the document")

if __name__ == "__main__":
    main()