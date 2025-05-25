from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

url=os.getenv('URL')
db=os.getenv('DB')
myclient = MongoClient(url)
mydb = myclient[db]
mycol = mydb["customers"]

def login_user(email,password):
    data=mycol.find_one({"Email Id":email,"Password":password})
    if data:
        return True
    return False

def register_user(data: dict):
    result = True if mycol.insert_one(data) else False
    return result


#print(register("raja","trj08012002@gmail.com",6369671812,"male","IT","AI","trj9543460192"))
#print(login("trj08012002@gmail.com","trj9543460192"))