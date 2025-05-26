from pymongo import MongoClient
import os
from dotenv import load_dotenv
from werkzeug.security import generate_password_hash,check_password_hash

def password_hash(password):
    return generate_password_hash(password)

def password_check(password, hashed_password):
    return check_password_hash(hashed_password, password)

load_dotenv()

url=os.getenv('URL')
db=os.getenv('DB')
myclient = MongoClient(url)
mydb = myclient[db]
mycol = mydb["customers"]

def login_user(email,password):
    data=mycol.find_one({"Email Id":email})
    if data:
        return data
    return None

def register_user(data: dict):
    result = True if mycol.insert_one(data) else False
    return result

def check_email(email):
    data = mycol.find_one({"Email Id": email})
    if data:
        return True 
    return False


#print(register("raja","trj08012002@gmail.com",6369671812,"male","IT","AI","trj9543460192"))
#print(login("trj08012002@gmail.com","trj9543460192"))