from fastapi import FastAPI
import uvicorn
#Инициализируем приложение
app = FastAPI()

#добавляем гет запрос
@app.get('/', summary='Главная ручка', tags=['Основные ручки!'])
def root():
    return "Hello World"


# Правильный запуск приложения
if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)