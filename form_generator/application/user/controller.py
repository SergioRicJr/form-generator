import time
from fastapi import APIRouter, Request, FastAPI

from fastapi.responses import JSONResponse
from google.oauth2 import id_token
from google.auth.transport import requests

google_request = requests.Request()

router = APIRouter()

@router.post("/users", tags=["Bankslip Batch"])
def create_user(request: Request):
    response = request.json()
    id_info = id_token.verify_oauth2_token(response.get('token'), google_request, '26016779977-ncd6go4kfkbfeermarclvbvndp2glaqo.apps.googleusercontent.com')
    print(id_info)

    return JSONResponse(
        content={"message": "Piece created", "data": 'request.model_dump()'}
    )


def configure(app: FastAPI):
    app.include_router(router)