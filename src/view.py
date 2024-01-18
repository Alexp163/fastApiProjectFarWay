from fastapi import Request
from fastapi.responses import HTMLResponse

from app import app
from templates import render_template


# Стартовая страница
@app.get("/")
async def index(request: Request):
    return render_template("index.html", request=request)


# каталог композиций
@app.get("/catalog")
def catalog(request: Request):
    return render_template("catalog.html", request=request)


# корзина с покупками
@app.get("/basket")
def basket(request: Request):
    return render_template("basket.html", request=request)

# страничка об авторе
@app.get("/author")
def author(request: Request):
    return render_template("author.html", request=request)


# контакты
@app.get("/contacts")
def contacts(request: Request):
    return render_template("contacts.html", request=request)


# лицензия
@app.get("/license")
def license(request: Request):
    return render_template("license.html", request=request)


# инструменты
@app.get("/tools")
def tools(request: Request):
    return render_template("tools.html", request=request)


# авторизация
@app.get("/login")
def login(request: Request):
    return render_template("login.html", request=request)


# регистрация
@app.get("/register")
def register(request: Request):
    return render_template("register.html", request=request)
