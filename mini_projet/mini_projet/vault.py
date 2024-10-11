import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# DICTIONNAIRE
vault = {
    'SECRET_KEY': os.getenv('SECRET_KEY'),
    'DEBUG': os.getenv('DEBUG', 'False') == 'True',
    'ALLOWED_HOSTS': os.getenv('ALLOWED_HOSTS').split(','),
}
