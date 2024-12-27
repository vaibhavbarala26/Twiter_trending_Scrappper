from pymongo import MongoClient
uri = "mongodb+srv://Hello:26022004@cluster0.dd8fs.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)
db = client["DB"]
collection = db["MY_Collection"]

