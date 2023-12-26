from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")


class User(BaseModel):
    username: str
    fullname: str
    email: str
    disabled: bool


class UserDB(User):
    password: str


users_db = {
    "greenheart": {
        "username": "greenheart",
        "fullname": "Juan Bogado",
        "email": "juancbogadoo@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    "greenheart2": {
        "username": "greenheart2",
        "fullname": "Juan Bogado",
        "email": "juancbogadoo2@gmail.com",
        "disabled": True,
        "password": "654321"
    }
}


def searchuser(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def search_user_db(username: str):
    if username in users_db:
        return User(**users_db[username])


async def current_user(token: str = Depends(oauth2)):
    user = searchuser(token)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciales inválidas",
            headers={"ww-auth": "Bearer"})
    if user.disabled:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Usuario Inactivo")
    return user


@router.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="El usuario no es correcto")

    user = search_user_db(form.username)
    if not form.password == user.password:
        raise HTTPException(
            status_code=status.HTTP_400_UNAUTHORIZED,
            detail="La contraseña no es correcta")

    return {"access_token": user.username, "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
