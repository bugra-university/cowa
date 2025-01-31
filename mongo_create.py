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
    # Define new project data
    new_project = {
        "name": "Research Project",
        "description": "This project focuses on measuring the durations of CRUD operations in MongoDB.",
        "manager": "John Doe",
        "budget": 200000,
        "createdAt": "2025-01-31T10:00:00Z",
        "updatedAt": "2025-01-31T10:00:00Z"
    }

    # Insert data into the collection
    result = collection.insert_one(new_project)

    # Record the end time **after successful insertion**
    end_time = time.time()

    # Print the results
    print(f"New project added! ID: {result.inserted_id}")
    print(f"Create operation time: {end_time - start_time:.6f} seconds")

except Exception as e:
    # If an error occurs, record end_time to avoid NameError
    end_time = time.time()
    print(f"An error occurred: {e}")
    print(f"Create operation failed after {end_time - start_time:.6f} seconds")
