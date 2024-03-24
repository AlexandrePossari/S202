from database import Database
from bookModel import BookModel

db = Database(database="relatorio_5", collection="books")
bookModel = BookModel(database=db)

def create_book():
    titulo = input("Enter book title: ")
    autor = input("Enter book author: ")
    ano = int(input("Enter publication year: "))
    preco = float(input("Enter book price: "))
    bookModel.create_book(titulo, autor, ano, preco)
    print("Book created successfully!")

def read_book_by_id():
    book_id = input("Enter book ID: ")
    book = bookModel.read_book_by_id(book_id)
    if book:
        print(f"Book details:\n {book}")
    else:
        print("Book not found.")

def update_book():
    book_id = input("Enter book ID to update: ")
    titulo = input("Enter new book title: ")
    autor = input("Enter new author: ")
    ano = input("Enter new publication year: ")
    preco = input("Enter new book price: ")

    updated_data = {}
    updated_data["titulo"] = titulo
    updated_data["autor"] = autor
    updated_data["ano"] = int(ano)
    updated_data["preco"] = float(preco)

    bookModel.update_book(book_id, **updated_data)
    print("Book updated successfully!")

def delete_book():
    book_id = input("Enter book ID to delete: ")        
    bookModel.delete_book(book_id)

def main_menu():
    while True:
        print("\nCRUD Menu: Books")
        print("1. Create Book")
        print("2. Read Book by ID")
        print("3. Update Book")
        print("4. Delete Book")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            create_book()
        elif choice == '2':
            read_book_by_id()
        elif choice == '3':
            update_book()
        elif choice == '4':
            delete_book()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()