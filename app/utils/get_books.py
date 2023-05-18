import os
from utils.request import RequestGetApi
from models.book_model import Book
import json


def search_books_api(query):

    print(f" => {query}")
    if not query:
        query = {"name": "flowers"}

    API_URLS = [
        ("https://www.googleapis.com/books/v1/volumes", {
            "q": query,
            "printType": "books",
            "maxResults": 10,
            "key":  os.getenv("GOOGLE_API_KEY")
        }), ("https://openlibrary.org/search.json", {"q": query})]
    fetches = []
    for url, params in API_URLS:
        fetch = RequestGetApi(url, params)
        fetches.append(fetch)

    [googleBooks, openLibraries] = fetches

    print(f" openlibrary => {openLibraries}")
    books = []
    for book in googleBooks["items"]:
        item = book["volumeInfo"]
        books.append(Book(title=item.get("title"), authors=item.get("authors"), subtitle=item.get("subtitle"), categories=item.get("categories"),
                          published_date=item.get("published_date"), publisher=item.get("publisher"), description=item.get("description"), image_links=item.get("imageLinks")))
    for item in openLibraries["docs"]:
        books.append(Book(title=item.get("title"), authors=item.get("author_name"), subtitle=item.get("subtitle"), categories=item.get("categories"),
                          published_date=item.get("publish_date"), publisher=item.get("publisher"), description=item.get("title_suggest"), image_links=item.get("imageLinks")))
    # for book in openLibraries.docs:
    #     books.append(Book(title=book.title, authors=book.authors, subtitle=book.subtitle, categories=book.categories,
    #                       published_date=book.published_date, publisher=book.published_date, description=book.description, image_links=book.imageLinks))

    return books
