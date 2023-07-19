import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
REP_LINK = os.getenv('REP_LINK')
YA_API_ID = os.getenv('YA_API_ID')
YA_API_KEY = os.getenv('YA_API_KEY')
YA_IAM_TOKEN = os.getenv('YA_IAM_TOKEN')