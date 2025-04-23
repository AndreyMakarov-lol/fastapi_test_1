from pydantic import BaseModel, Field, EmailStr, ConfigDict
#Field фильтры для полей, EmailStr рповеряет корректность email

data_no_age ={
    'email': 'govno@jopa.sru',
    'bio': "1234567890"
}
data_age ={
    'email': 'govno@jopa.sru',
    'bio': "1234567890",
    'age': 12,
    'gender' : 'male'
}

class UserSchema(BaseModel):
    email: EmailStr
    bio: str | None = Field(max_length=10) #Максимальная длинна данных




class UserAgeSchema(UserSchema):    # Наследуем от UserSchema оставляем данные и добавляем новые
    age: int = Field(ge=0, le=130) #ge не меньше или равно, le не больше или равно

    model_config = ConfigDict(extra='forbid') # Запрет лишних полей, вылет с ошибкой




user = UserSchema(**data_no_age)
user_age = UserAgeSchema(**data_age)
print(repr(user)) # repr выводит имя функции дающей ответ
print(repr(user_age))