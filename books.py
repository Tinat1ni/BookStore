from faker import Faker
import random
from datetime import datetime

fake = Faker()
categories = ['Fiction', 'Horror', 'Science', 'History',
              'Biography', 'Fantasy', 'Mystery', 'Romance']
today = datetime.today().date()


class Book:
    def __init__(self, title, category, number_of_pages,
                 publication_date, author_id):
        self.title = title
        self.category = category
        self.number_of_pages = number_of_pages
        self.publication_date = publication_date
        self.author_id = author_id


    @staticmethod
    def generate_fake_book(author_id):
        return Book(
            title=fake.sentence(nb_words=4),
            category=random.choice(categories),
            number_of_pages=fake.random_int(min=100, max=1600),
            publication_date=fake.date_between_dates(date_start=fake.date_of_birth(), date_end=today),
            author_id=author_id
        )

    def save(self, cursor):
        cursor.execute('''
            INSERT INTO books (title, category, number_of_pages,
             publication_date, author_id)
             VALUES (?, ?, ?, ?, ?)
             ''', (self.title, self.category, self.number_of_pages,
                   self.publication_date, self.author_id))

