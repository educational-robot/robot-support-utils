from fastapi import APIRouter, HTTPException
from fastapi.responses import FileResponse

from server.core.config import config
from server.dto.request import TakePictureRequest
from server.service import camera_service

router = APIRouter(
    prefix="/camera",
    tags=["Camera"]
)

@router.get("/take-picture")
def take_picture(take_picture_request: TakePictureRequest):
    if take_picture_request.api_key != config.API_KEY:
        raise HTTPException(
            status_code=401,
            detail=f"API key missing."
        )

    path = camera_service.take_picture()
    if path is None:
        raise HTTPException(
            status_code=500,
            detail=f"Error taking picture."
        )

    return FileResponse(path, media_type="image/jpeg")

@router.get("/take-video")
def take_video(take_picture_request: TakePictureRequest):
    if take_picture_request.api_key != config.API_KEY:
        raise HTTPException(
            status_code=401,
            detail=f"API key missing."
        )

    path = camera_service.take_video()
    if path is None:
        raise HTTPException(
            status_code=500,
            detail=f"Error taking picture."
        )

    return FileResponse(path, media_type="video/mp4")