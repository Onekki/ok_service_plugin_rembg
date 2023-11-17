from fastapi import APIRouter, Response
from pydantic import BaseModel

import rembg
import requests

class Image(BaseModel):
    url: str

router = APIRouter(
    prefix="/api/rembg"
)

@router.post("/single")
async def single(image: Image):
    response = requests.get(image.url)
    model_name = "isnet-general-use"
    session = rembg.new_session(model_name)
    bytes = rembg.remove(response.content, session=session)
    return Response(content=bytes, media_type='image/png')
