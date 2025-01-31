import time
from pymongo import MongoClient
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Get MongoDB URI from .env file
MONGO_URL = os.getenv("MONGO_URI")

# Check if MongoDB URI is available
if not MONGO_URL:
    raise ValueError("MongoDB URI not found in .env file")

# Create the connection
client = MongoClient(MONGO_URL)

# Select database and collection
db = client["db"]
collection = db["projects"]

# Record the start time
start_time = time.time()

try:
    # Data to delete
    query = {"name": "Research Project"}

    # Delete data
    result = collection.delete_one(query)

    # Record the end time
    end_time = time.time()

    # Print operation time
    print(f"Delete operation time: {end_time - start_time:.6f} seconds")
    print(f"Deleted {result.deleted_count} document(s).")

except Exception as e:
    print(f"An error occurred: {e}")
