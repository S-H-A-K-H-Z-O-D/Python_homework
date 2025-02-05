from fastapi import FastAPI
from database import engine, Base
from routers import posts, comments, users

# Initialize Database
Base.metadata.create_all(bind=engine)

# Create App
app = FastAPI()

# Include Routers
app.include_router(posts.router)
app.include_router(comments.router)
app.include_router(users.router)
