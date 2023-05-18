import os
from dotenv import load_dotenv
from flask import Flask
from config.database import mongo
from flask_graphql import GraphQLView
from book_graphql.query import schema

load_dotenv()


def main():
    app = Flask(__name__)

    app.config["MONGO_URI"] = os.getenv("MONGO_URI")
    mongo.init_app(app)
    app.add_url_rule(
        '/books', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

    app.run(debug=os.getenv("DEBUG"))

# @app.before_request
# def create_data():
#     BookService.create_book()


if __name__ == "__main__":
    main()
