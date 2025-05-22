#Create Database and collection
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#Get the all databases
data_base_list=myclient.list_database_names()
#Get the all collection
mydb = myclient["mydatabase"]
collection_names_list=mydb.list_collection_names()
print(data_base_list)
print(collection_names_list)
