from fastapi import FastAPI

from controllers import auth, post
from databases import database, engine, metadata

@asynccountextmanager
async def lifespan(app: FastAPI):
    from models.post import posts

    await database.connect()
    metadata.create_all(engine)
    yield
    await database.disconnect()

app = FastAPI(lifespan=lifespan)
app.include_router(auth.router)
app.include_router(post.router)