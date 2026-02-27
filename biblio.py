import Book as b
import Library as l
import random
import time

library = l.FastLibrary()
for num in range(100000):
    new_book  = b.Book(f"Book{num}")
    library.add_book(new_book)

start = time.time()
for i in range(1, 500):
    numero = random.randint(0, 150000)
    library.find_books_by_name(f"Book{numero}")
end = time.time()

total_time = end-start

start = time.time()
for i in range(1, 500):
    numero = random.randint(0, 150000)
    library.find_books_by_name_fast(f"Book{numero}")
end = time.time()

total_time_fast = end-start
print(f"Total time: {total_time:.4f} seconds\nTotal time (FAST VERSION): {total_time_fast:.4f} seconds")