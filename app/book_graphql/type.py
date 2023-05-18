from graphene import ObjectType, String, List


class BookType(ObjectType):
    id = String()
    title = String()
    subtitle = String()
    authors = List(String)
    categories = List(String)
    publication_date = String()
    editor = String()
    description = String()
    image = String()
    resource = String()
