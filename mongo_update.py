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

# Update operation start time
start_time = time.time()

try:
    # Data to update
    query = {"name": "Research Project"}
    new_values = {"$set": {"budget": 250000}}

    # Find and update the document
    result = collection.update_one(query, new_values)

    # Update operation end time
    end_time = time.time()

    # Print processing time
    print(f"Update operation time: {end_time - start_time:.6f} seconds")

    # Print update status
    if result.modified_count > 0:
        print(f"Updated {result.modified_count} document(s).")
    else:
        print("No document was updated. Check if the document exists.")

except Exception as e:
    print(f"An error occurred: {e}")
