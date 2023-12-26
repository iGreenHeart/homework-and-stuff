from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter(prefix="/user",
                   tags=["user"],
                   responses={404: {"message": "not found"}})


class User(BaseModel):
    id: int
    name: str
    surname: str
    age: int


user_list = [User(id=1, name="JC", surname="B", age=22),
             User(id=2, name="N", surname="B", age=32),
             User(id=3, name="JR", surname="B", age=55)]


@router.get("/")
async def users():
    return user_list


@router.get("/{id}")
async def user(id: int):
    return search_user(id)


@router.get("/")
async def user(id: int):
    return search_user(id)


@router.post("/", response_model=User, status_code=201)
async def user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="El usuario ya existe")
    else:
        user_list.append(user)
        return user


@router.put("/")
async def user(user: User):
    found = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == user.id:
            user_list[index] = user
            found = True

    if not found:
        return {"error": "No se ha actualizado el usuario."}
    else:
        return user


@router.delete("/{id}")
async def user(id: int):
    found = False
    for index, saved_user in enumerate(user_list):
        if saved_user.id == id:
            del user_list[index]
            found = True
    if not found:
        return {"error": "No se ha eliminado el usuario."}


def search_user(id: int):
    users = filter(lambda user: user.id == id, user_list)
    try:
        return list(users)[0]
    except:
        return {"error": "no se encontró un usuario"}
