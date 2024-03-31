from fastapi.templating import Jinja2Templates
from fastapi import APIRouter

from dotenv import load_dotenv
import os

load_dotenv()

router = APIRouter()

timezone = 'UTC'

templates = Jinja2Templates(directory="app/templates")

# JWT authentication
SECRET_KEY = os.environ.get('SECRET_KEY', 'secret-key')
ALGORITHM = os.environ.get('ALGORITHM', 'HS256')
ACCESS_TOKEN_EXPIRE_MINUTES = 30