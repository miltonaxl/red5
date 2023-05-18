from datetime import datetime
from bson.objectid import ObjectId


class Book:
    def __init__(self, title, authors, categories, published_date, publisher, description, subtitle=None, image_links=None, _id=None, created_at=None, updated_at=None):
        self.id = _id
        self.title = title
        self.subtitle = subtitle
        self.authors = authors
        self.categories = categories
        self.published_date = published_date
        self.publisher = publisher
        self.description = description
        self.image_links = image_links
        self.created_at = created_at
        self.updated_at = updated_at

    @classmethod
    def from_dict(cls, adit):
        return cls(
            adit.get('title'),
            adit.get('subtitle'),
            adit.get('authors'),
            adit.get('categories'),
            adit.get('published_date'),
            adit.get('publisher'),
            adit.get('description'),
            adit.get('image_links'),
            _id=adit.get('_id') and ObjectId(adit['_id']),
            created_at=adit.get('created_at') and datetime.fromisoformat(
                adit['created_at']),
            updated_at=adit.get('updated_at') and datetime.fromisoformat(
                adit['updated_at']),
        )

    def to_dict(self):
        return {
            '_id': ObjectId(),
            'title': self.title,
            'subtitle': self.subtitle,
            'authors': self.authors,
            'categories': self.categories,
            'published_date': self.published_date,
            'publisher': self.publisher,
            'description': self.description,
            'image_links': self.image_links,
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
        }

    def __setitem__(self, key, value):
        setattr(self, key, value)
