from fastapi import FastAPI
from fastapi.responses import JSONResponse
from routes.user_routes import router as user_router
from db import get_db, DATABASE_URL
from sqlalchemy import create_engine
from models import Base

app = FastAPI()

# Create database tables if they don't exist
engine = create_engine(DATABASE_URL)
Base.metadata.create_all(engine)

@app.get("/")
def read_root():
    return JSONResponse(content={"Hello": "World"})

app.include_router(user_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)