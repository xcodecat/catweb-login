from wire import Wire, Request
from wire.static import StaticFiles
from wire.templating import FoxTemplates

app = Wire()
app.mount(StaticFiles("./public"), "/public") 

@app.get('/test')
async def index():
    return 'Hello World!'