from database import DataBase
from authors import Author
from books import Book
from queries import Queries
import random

db = DataBase()
db.create_tables()

authors = []
for _ in range(500):
    author = Author.generate_fake_author()
    author.save(db.cursor)
    authors.append(author)

db.connection.commit()

db.cursor.execute('SELECT id FROM authors')
author_ids = [row[0] for row in db.cursor.fetchall()]

for _ in range(1000):
    book = Book.generate_fake_book(author_id=random.choice(author_ids))
    book.save(db.cursor)

db.connection.commit()

max_pages = Queries.get_book_with_max_pages(db.cursor)
average_pages = Queries.get_average_number_of_pages(db.cursor)
youngest = Queries.get_youngest_author(db.cursor)
authors_with_no_books = Queries.get_authors_with_no_books(db.cursor)
authors_with_more_than_three_books = Queries.get_authors_with_more_than_three_books(db.cursor)

print(f'Book that has maximum number of pages:\nid:{max_pages[0]}\ntitle:{max_pages[1]}\nCategory:{max_pages[2]}\nnumber of pages:{max_pages[3]}\npublished on {max_pages[4]}\nauthor id: {max_pages[5]}\n')
print(f'average pages: {int(average_pages)}\n')
print(f'The youngest author is {youngest[0]} {youngest[1]}\n')

if authors_with_no_books:
    print('Some of the authors with no books:')
    for author in authors_with_no_books:
        print(f"{author[0]} {author[1]}")
else:
    print('There is no one without a book\n')

if authors_with_more_than_three_books:
    print('\nAuthors with more than 3 books:')
    for author in authors_with_more_than_three_books:
        print(f'{author[0]} {author[1]} - {author[2]} books')
else:
    print('No authors with more than 3 books found')


db.close()

