from fastapi import FastAPI

app = FastAPI()

books = [
    {
        "id": 1,
        "title": "Python Basic",
        "author": "Nguyen Van A",
        "category": "programming",
        "year": 2022,
        "is_available": True
    },
    {
        "id": 2,
        "title": "Web API Design",
        "author": "Tran Van B",
        "category": "web",
        "year": 2021,
        "is_available": False
    }
]

def return_book(books: list, is_available=True):
    books_re = []
    for book in books:
        if book["is_available"] == is_available:
            books_re.append(book)
    return books_re


@app.get("/books/available")
def get_available_books():
    result = return_book(books)
    return {
        "status": "Success",
        "message": "Get success",
        "books": result
    }


@app.get("/books/borrowed")
def get_borrowed_books():
    result = return_book(books, is_available=False)
    return {
        "status": "Success",
        "message": "Get success",
        "books": result
    }