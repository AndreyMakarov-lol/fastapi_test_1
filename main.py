from fastapi import FastAPI, HTTPException
import uvicorn
from pydantic import BaseModel

#Инициализируем приложение
app = FastAPI()

books = [
    {
        'id': 1,
        'title': 'Асинхронность в пайтон',
        'author': 'Меттью'
    },
    {
        'id': 2,
        'title': 'Бэкенд разработка в Python',
        'author': 'Артём'
    }
]

@app.get('/books', tags=['Книги'], summary="Получить все книги")
def read_books():
    return books

@app.get('/books/{book_id}', tags=['Книги'], summary="Получить конкретную книгу")
def read_book(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code=404, detail="Книга не найдена")


class NewBook(BaseModel):
    title: str
    author: str



@app.post('/books')
def create_book(new_book: NewBook):
    books.append({
        'id': len(books) +1,
        'title': new_book.title,
        'author': new_book.author,
    })
    return {'success': True}






# Правильный запуск приложения
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)