from book_data import load_books , save_books
def search_book():

    books = load_books()
    if not books:
        print("No book is available")
    else:
        isbn =input("Enter isbn code for search book:")
        for book  in books:
            if book["isbn"] == isbn:
                print(f"Title: {book['title']}")
                print(f"Author: {book['author']}")
                print(f"ISBN: {book['isbn']}")
                print(f"Genre: {book['genre']}")
                print(f"Price: ${book['price']}")
                print(f"Stock: {book['quantity']} copies")
                print("-" * 50)
        else:
            print("Enter correct isbn number")