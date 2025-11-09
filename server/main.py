from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from server.core.config import config
from server.routers import camera
from server.service import camera_service


@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- Startup ---
    print("On Startup")
    camera_service.listen_redis_command()

    yield  # App chạy tại đây

    # --- Shutdown ---
    print("🛑 App shutting down...")

app = FastAPI(lifespan=lifespan)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# routers
app.include_router(camera.router, prefix=config.BASE_URL)