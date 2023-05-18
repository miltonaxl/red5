def add_resource_property(book):
    book_dict = vars(book)
    book_dict["resource"] = "DATABASE"
    return book_dict
