from book_data import load_books , save_books

def views_books():
    books = load_books()
    if not books:
        print("book is not available")
    else:
        for book in books:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"ISBN: {book['isbn']}")
            print(f"Genre: {book['genre']}")
            print(f"Price: ${book['price']}")
            print(f"Stock: {book['quantity']} copies")
            print("-" * 50)

        else:
            print("books are not available")

