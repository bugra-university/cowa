from pymongo import MongoClient
from dotenv import load_dotenv
import os

# .env dosyasını yükle
load_dotenv()

# MongoDB URI'sini al
uri = os.getenv("MONGO_URI")

try:
    # MongoDB'ye bağlan
    client = MongoClient(uri)
    db = client["db"]  # Veritabanı adı "db"
    print("✅ MongoDB bağlantısı başarılı!")

    # Koleksiyon örneği
    projects_collection = db["projects"]
    for document in projects_collection.find():
        print(document)
except Exception as e:
    print(f"❌ MongoDB bağlantısı başarısız: {e}")
