import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    FASTAPI_URL = os.environ.get('FASTAPI_URL') or 'http://192.168.1.123'