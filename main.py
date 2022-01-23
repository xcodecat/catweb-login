from wire import Wire, Request
from wire.static import StaticFiles
from wire.templating import FoxTemplates
from wire.response import HTMLResponse

def convert(body: bytes) -> dict:
    dct: dict = dict()
    dct.update(tupl for tupl in [(k, v) for k, v in [row.split("=") for row in (body.decode("utf-8")).split("&")]])
    return dct

app = Wire()
app.mount(StaticFiles("./public"), "/public") 

@app.get('/login')
async def login(req: Request):
    with open("login.html", "r") as f:
        data = f.read()
    return HTMLResponse(data)

@app.post("/login")
async def post_login(req: Request):
    data = convert(await req.body())
    if data["password"] == "123" and data["username"] == "laura":
        with open("after-login.html", "r") as f:
            return HTMLResponse(f.read())
    print(data)