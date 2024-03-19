from fastapi.templating import Jinja2Templates
from fastapi import APIRouter

router = APIRouter()

timezone = 'Asia/Tehran'

templates = Jinja2Templates(directory="app/templates")