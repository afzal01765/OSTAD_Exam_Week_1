from logging import exception
from book_data import load_books , save_books

def add_book():
    books = load_books()
    title = input("Enter book title: ").strip()
    author = input("Enter author name: ").strip()
    isbn = input("Enter ISBN (must be unique): ").strip()
    genre = input("Enter genre: ").strip()

    try:
        price =float(input("Enter book Price:"))
        if price<0:
            raise ValueError("Enter possitive value")
        quantity = int(input("Enter quantity in stock: "))
        if quantity < 0:
            raise ValueError("Quantity must be a non-negative integer.")
    except ValueError as e:
        print(f"Error{e}")
        return
    for book in books:
        if book["isbn"]  ==isbn:
            print("Error: A book with this ISBN already exists!")
            return
    data = {
        "title":title ,
        "author":author,
        "isbn":isbn,
        "genre":genre,
        "price":price,
        "quantity":quantity
    }
    books.append(data)
    save_books(books)
    
