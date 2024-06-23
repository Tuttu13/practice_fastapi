# (1) 必要なライブラリをインポートする
import strawberry
from fastapi import FastAPI
from strawberry.asgi import GraphQL


@strawberry.type
class Book:
    name: str
    created_year: int


@strawberry.type
class Query:
    @strawberry.field
    def book_a(self) -> Book:
        return Book(name="HEART", created_year=2000)

    @strawberry.field
    def book_b(self) -> Book:
        return Book(name="HEAD", created_year=1900)


schema = strawberry.Schema(query=Query)

graphql_app = GraphQL(schema)

app = FastAPI()
app.add_route("/graphql", graphql_app)
