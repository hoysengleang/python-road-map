from os import name


class books :

    def __init__(self, title, author, isbn, price, is_available) -> None:
        self.title  = title
        self.author = author
        self.isbn   = isbn
        self.price  = price
        self.is_available = is_available
    

class FictionBook(books):

    def __init__(self, title, author, isbn, price, is_available, genre):

        super().__init__(title, author, isbn, price, is_available)

        self.genre = genre


    def get_info(self):

        return f"{super().get_info()} - Genre: {self.genre}"

    def calculate_late_fee(self, days_late):

        return days_late * 0.50

    


class TechnicalBook(books):

    def __init__(self, title, author, isbn, price, is_available, edition, topic):
        super().__init__(title, author, isbn, price, is_available)
        self.edition = edition
        self.topic = topic
    
    def get_info(self):
        return f"{super().get_info()} - Edition: {self.edition}, Topic: {self.topic}"


    def calculate_late_fee(self, days_late):
        return days_late * 0.25





class Library:

    def __init__(self, name) -> None:
        self.name = name
        self.books = []

    def add_book(self, books) :
        self.books.append(books)
        print("books added successfully", books.title)


    def list_available_books(self):
        available_books = []
        index = 1
        for book in self.books:
            if book.is_available:
                available_books.append(book)
                index += 1
        return f"Available books: {available_books} at index {index}"

    def borrow_book(self, isbn):

        for book in self.books:

            if book.isbn == isbn and book.is_available:

                book.is_available = False

                print("book borrowed successfully", book.title)

                return "book borrowed successfully"

        return "book not found or not available"



    




if __name__ == "__main__":

    Library = Library("My Library")

    book1 = FictionBook("The Great Gatsby", "F. Scott Fitzgerald", "9780743273565", 10.99, True, "Fiction")
    book2 = TechnicalBook("Python Programming", "John Doe", "9780132356188", 15.99, True, "1st Edition", "Programming")

    Library.add_book(book1)
    Library.add_book(book2)

    print(Library.list_available_books())
        

            
            