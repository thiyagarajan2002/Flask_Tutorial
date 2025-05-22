#Create Database and collection
from connection import mydb



def store(dic : dict):
    mycol=mydb["customers"]
    if dic and dic["name"]:
        x=mycol.insert_one(dic)
        print(x)
    else:
        print("Data not available")

def read(name : str):
    mycol=mydb["customers"]
    user=mycol.find_one(
        {"name":name}
    )
    if user and user["name"]:
        return user
    else:
        return f"User doesn't found"

def update(name :str,update_data:dict):
    mycol=mydb["customers"]
    result=mycol.update_one(
        {"name":name},
        {"$set":update_data}
        )
    #print(result)

    if result.matched_count>0:
        if result.modified_count>0:
            print("Updated")

def delete(name: str):
    mycol=mydb['customers']
    result=mycol.delete_one({"name":name})
    print(result)

def main():
    dic={
        "name":"raja",
        "age":"23"
    }
    store(dic)
    print(read("raja"))
    update("raja",{"age":"25"})
    delete('raja')
if __name__=="__main__":
    main()
