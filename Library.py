class Library:
    def __init__(self):
        self.library = []
    
    def add_book(self, book):
        self.library.append(book)
    
    def find_books_by_name(self, name):
        trovato = False
        for books in self.library:
            if books.name == name:
                print(f"Book {name} found in the library")
                trovato = True
        if trovato is False:
            print("Book not found in the archive")

class FastLibrary(Library):
    def __init__(self):
        super().__init__()
        self.dictionary = {}
    
    def add_book(self, book):
        super().add_book(book)
        self.dictionary[book.name] = book
    
    def find_books_by_name_fast(self, name):
        found = self.dictionary.get(name)
        if found:
            print(f"Book {name} found in the library")
        else:
            print("Book not found in the archive")                    