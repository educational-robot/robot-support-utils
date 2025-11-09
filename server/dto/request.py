from pydantic import BaseModel


class TakePictureRequest(BaseModel):
    api_key: str