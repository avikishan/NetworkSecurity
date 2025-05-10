
from pymongo.mongo_client import MongoClient
from dotenv import load_dotenv
import os
load_dotenv()

# for key, value in os.environ.items():
#     print(f"{key}={value}")

uri = os.getenv("MONGO_DB_URL").encode('utf-8').decode('unicode_escape')
print(uri)

# Create a new client and connect to the server
client = MongoClient(uri)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)