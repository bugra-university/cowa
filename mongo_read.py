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

# Read operation start time
start_time = time.time()

try:
    # Get all projects
    all_projects = list(collection.find())

    # Read operation end time
    end_time = time.time()

    # Print retrieved documents
    if all_projects:
        for project in all_projects:
            print(project)
    else:
        print("No projects found.")

    # Print operation time
    print(f"Read operation time: {end_time - start_time:.6f} seconds")

except Exception as e:
    print(f"An error occurred: {e}")
