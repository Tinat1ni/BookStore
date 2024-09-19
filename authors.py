from faker import Faker

fake = Faker()

class Author:
    def __init__(self, name, last_name, date_of_birth, birth_place):
        self.name = name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.birth_place = birth_place


    @staticmethod
    def generate_fake_author():
        return Author(
            name=fake.first_name(),
            last_name=fake.last_name(),
            date_of_birth=fake.date_of_birth(),
            birth_place=fake.city()
        )


    def save(self, cursor):
        cursor.execute('''
            INSERT INTO authors (name, last_name, 
                                 date_of_birth, birth_place)
            VALUES (?, ?, ?, ?)
        ''', (self.name, self.last_name,
              self.date_of_birth, self.birth_place))


