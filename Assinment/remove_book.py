from book_data import load_books , save_books

def search_book_by_id(isbn):
    books = load_books()
    for book  in books:
        if book["isbn"] == isbn:
            return book

def remove_book():

    books = load_books()
    isbn =input("Enter Isbn number:")

    for book in books:
        if book["isbn"] == isbn:
            books.remove(search_book_by_id(isbn))

