import json
import os

BOOKS_FILE = "books.json"
quintity_stock = 0

def load_books():
    """Load books from the JSON file or return an empty list if the file doesn't exist."""
    if not os.path.exists(BOOKS_FILE):
        return []
    with open(BOOKS_FILE, "r", encoding="utf-8") as file:
        return json.load(file)

def save_books(books):
    """Save the book list to the JSON file."""
    with open(BOOKS_FILE, "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)
