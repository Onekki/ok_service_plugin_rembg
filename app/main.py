from fastapi import FastAPI

from routers import rembg

app = FastAPI()

app.include_router(rembg.router)

@app.get("/")
def index():
    return "Hello World!"


if __name__=="__main__":
    import uvicorn
    uvicorn.run(app,
        host="127.0.0.1",
        port=8888
    )
