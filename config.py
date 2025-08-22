import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'dev_key_recipe_recommender')
    SPOONACULAR_API_KEY = os.getenv('SPOONACULAR_API_KEY', 'mock_key')
    SPOONACULAR_BASE_URL = 'https://api.spoonacular.com'
    USE_MOCK_DATA = os.getenv('USE_MOCK_DATA', 'True').lower() == 'true'