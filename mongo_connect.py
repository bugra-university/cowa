from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()

# Get MongoDB URI
uri = os.getenv("MONGO_URI")

try:
    # Connect to MongoDB
    client = MongoClient(uri)
    db = client["db"]  # Database name "db"
    print("✅ MongoDB connection successful!")

    # Collection instance
    projects_collection = db["projects"]
    for document in projects_collection.find():
        print(document)
except Exception as e:
    print(f"❌ MongoDB connection failed: {e}")
