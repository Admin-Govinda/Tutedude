from pymongo import MongoClient

try:
    client = MongoClient("mongodb+srv://Well2025:Don2025W@cluster0.5z1lm5k.mongodb.net/test_db?retryWrites=true&w=majority&appName=Cluster0")
    client.admin.command("ping")
    print("✅ Connected successfully to MongoDB Atlas!")
except Exception as e:
    print("❌ Connection failed:", e)
