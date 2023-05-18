from repository.repository import BookRepository
from utils import index, get_books
import re


class BookService:

    @staticmethod
    def search_api_books(self, query):
        books = get_books.search_books_api(query)
        results = []
        for book in books:
            id = BookRepository.create_book(self, book)
            book = vars(book)
            book = ({**book, "id": id, "resource": "API"})
            results.append(book)
        return results

    @staticmethod
    def get_all_books(self):
        books = BookRepository.get_all_books(self)
        books = list(map(index.add_resource_property, books))
        if len(books) == 0:
            books = BookService.search_api_books(self, {})
        return books

    @staticmethod
    def get_book_by_id(self, id):
        book = BookRepository.get_book_by_id(self, id)
        book = vars(book)
        book = {**book, "resource": "DATABASE"}
        return book

    @staticmethod
    def delete_book(self, id):
        return BookRepository.get_book_by_id(self, id)

    @staticmethod
    def search_by_query(self, query, value):

        regex_value = f'.*{re.escape(value)}.*'
        regex_query = {query: {'$regex': regex_value, '$options': 'i'}}
        books = BookRepository.search_by_query(self, regex_query)
        books = list(map(index.add_resource_property, books))
        if len(books) == 0:
            books = BookService.search_api_books(self, {query: value})

        return books
