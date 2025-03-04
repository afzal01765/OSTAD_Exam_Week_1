import add_book
import view_book
import search_book
import remove_book

def main():
    while True:
        print("\nBook Store Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Search Book")
        print("4. Remove Book")
        print("5. Exit")

        choice = input("Enter your choice: ").strip()
        if choice == "1":
            add_book.add_book()
        elif choice == "2":
            view_book.views_books()
        elif choice == "3":
            search_book.search_book()
        elif choice == "4":
            remove_book.remove_book()
        elif choice == "5":
            print("Exiting... Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")

if __name__ == "__main__":
    main()
