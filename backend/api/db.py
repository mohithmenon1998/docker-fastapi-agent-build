import os
from dotenv import load_dotenv
load_dotenv()


DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("oops!...No Value found for 'DATABASE_URL', please check your env file.")
   
print(DATABASE_URL) 