from typing import Annotated

from fastapi import APIRouter
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
    with open('output.png', 'wb') as o:
        model_name = "isnet-general-use"
        session = rembg.new_session(model_name)
        output = rembg.remove(response.content, session=session)
        o.write(output)
        return image
