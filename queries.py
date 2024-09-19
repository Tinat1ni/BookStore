class Queries:
    @staticmethod
    def get_book_with_max_pages(cursor):
        cursor.execute('''
                    SELECT * FROM books 
                    ORDER BY number_of_pages DESC
                    LIMIT 1
            ''')
        return cursor.fetchone()


    @staticmethod
    def get_average_number_of_pages(cursor):
        cursor.execute('''
                SELECT AVG(number_of_pages)
                FROM books
            ''')
        return cursor.fetchone()[0]


    @staticmethod
    def get_youngest_author(cursor):
        cursor.execute('''
                SELECT name, last_name FROM authors
                ORDER BY date_of_birth DESC
                LIMIT 1
            ''')
        return cursor.fetchone()


    @staticmethod
    def get_authors_with_no_books(cursor):
        cursor.execute('''
                SELECT a.name, a.last_name 
                FROM authors a
                LEFT JOIN books b ON a.id = b.author_id
                WHERE b.id IS NULL
                LIMIT 10
            ''')
        return cursor.fetchall()


    @staticmethod
    def get_authors_with_more_than_three_books(cursor):
        cursor.execute('''
                SELECT a.name, a.last_name, COUNT(b.id) as book_count
                FROM authors a
                JOIN books b ON a.id = b.author_id
                GROUP BY a.id
                HAVING book_count > 3
                LIMIT 5
            ''')
        return cursor.fetchall()
