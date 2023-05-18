from graphene import ObjectType, String, List, Field, Schema, Boolean, Mutation
from book_graphql.type import BookType
from services.book_service import BookService
from auth import generate_jwt
from auth.decorator import authentication_required


class GenerateTokenMutation(Mutation):
    class Arguments:
        username = String(required=True)

    token = String()

    def mutate(self, info, username):
        if username == "red5":
            token = generate_jwt.generate_token(username)
            return GenerateTokenMutation(token=token)
        else:
            raise Exception("Credenciales inválidas")


class DeleteBookMutation(Mutation):
    class Arguments:
        id = String(required=True)

    success = Boolean()

    @authentication_required
    def mutate(self, info, id):
        BookService.delete_book(self, id)
        success = True

        return DeleteBookMutation(success=success)


class Mutation(ObjectType):
    generate_token = GenerateTokenMutation.Field()
    delete_book = DeleteBookMutation.Field()


class Query(ObjectType):
    book_list = List(BookType)
    book_by_id = Field(BookType, id=String(required=True))
    books_by_property = List(BookType, query=String(
        required=True), value=String(required=True))

    @authentication_required
    def resolve_book_list(self, info):
        return BookService.get_all_books(self)

    @authentication_required
    def resolve_book_by_id(self, info, id):
        return BookService.get_book_by_id(self, id)

    @authentication_required
    def resolve_books_by_property(self, info, query, value):
        return BookService.search_by_query(self, query, value)


schema = Schema(query=Query, mutation=Mutation)
