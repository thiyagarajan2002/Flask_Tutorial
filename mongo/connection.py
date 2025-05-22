from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()
db_url=os.getenv('DB_CONN')
database=os.getenv('DB_NAME')
myclient = MongoClient(db_url)
mydb=myclient[database]
