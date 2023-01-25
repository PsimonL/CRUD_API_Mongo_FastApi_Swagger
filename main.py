import uvicorn as uvicorn
from fastapi import FastAPI

import server.routes

app = FastAPI()
app.include_router(server.routes.router)

if __name__ == "__main__":
    # 127.0.0.1:8080/docs
    # Go docs, then check out CRUD methods for certain routes - "Try it out" option
    # uvicorn.run("server.routes:router", port=8080, reload=True)
    uvicorn.run("main:app", port=8080, reload=True)
