from wire import Wire, Request
from wire.static import StaticFiles
from wire.templating import FoxTemplates
from wire.response import HTMLResponse

app = Wire()
app.mount(StaticFiles("./public"), "/public") 

@app.get('/login')
async def login(req: Request):
    with open("login.html", "r") as f:
        data = f.read()
    return HTMLResponse(data)

@app.post("/login")
async def post_login(req: Request):
  data = await req.body()
  print(data)