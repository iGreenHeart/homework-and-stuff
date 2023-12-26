from fastapi import APIRouter, Depends, HTTPException, status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from passlib.context import CryptContext
from datetime import datetime, timedelta

ALGORITHM = "HS256"
ACCESS_TOKEN_DURATION = 1
SECRET = "bae46ac1c35a6078fc99ffc7e33afd48a0e7ea4be6a2c41de094d731afd2ffd8"

router = APIRouter()

oauth2 = OAuth2PasswordBearer(tokenUrl="login")

crypt = CryptContext(schemes=["bcrypt"])


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
        "password": "$2a$12$B2Gq.Dps1WYf2t57eiIKjO4DXC3IUMUXISJF62bSRiFfqMdOI2Xa6"
    },
    "greenheart2": {
        "username": "greenheart2",
        "fullname": "Juan Bogado",
        "email": "juancbogadoo2@gmail.com",
        "disabled": True,
        "password": "$2a$12$SduE7dE.i3/ygwd0Kol8bOFvEABaoOOlC8JsCSr6wpwB4zl5STU4S"
    }
}


def search_user_db(username: str):
    if username in users_db:
        return UserDB(**users_db[username])


def searchuser(username: str):
    if username in users_db:
        return User(**users_db[username])


async def auth_user(token: str = Depends(oauth2)):

    exception401 = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Credenciales inválidas",
        headers={"ww-auth": "Bearer"})

    try:
        username = jwt.decode(token, SECRET, algorithms=[ALGORITHM]).get("sub")
        if username is None:
            raise exception401

    except JWTError:
        raise exception401

    return searchuser(username)


async def current_user(user: User = Depends(auth_user)):
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

    if not crypt.verify(form.password, user.password):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="La contraseña no es correcta")

    access_token = {"sub": user.username,
                    "exp": datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_DURATION)}

    return {"access_token": jwt.encode(access_token, SECRET, algorithm=ALGORITHM), "token_type": "bearer"}


@router.get("/users/me")
async def me(user: User = Depends(current_user)):
    return user
