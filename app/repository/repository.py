from config.database import mongo
from bson.objectid import ObjectId
from typing import List
from models.book_model import Book


class BookRepository:
    def create_book(self, book: Book) -> str:
        result = mongo.db.books.insert_one(book.to_dict())
        return str(result.inserted_id)

    def get_all_books(self) -> List[Book]:
        books = mongo.db.books.find()
        result = []
        for book in books:
            result.append(Book.from_dict(
                book))
        return result

    def get_book_by_id(self, book_id: str) -> Book:
        book = mongo.db.books.find_one({'_id': ObjectId(book_id)})

        return Book.from_dict(book)

    def delete_book(self, book_id: str) -> str:
        return mongo.db.books.delete_one({'_id': ObjectId(book_id)})

    def search_by_query(self, query) -> List[Book]:
        book_dicts = mongo.db.books.find(query)
        return [Book.from_dict(book_dict) for book_dict in book_dicts]
