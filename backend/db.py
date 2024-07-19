import asyncio
from motor.motor_asyncio import AsyncIOMotorClient
import os
from dotenv import load_dotenv

load_dotenv()

client = None
database = None

async def connect_to_mongo():
    global client, database
    mongo_conn_str = os.getenv("MONGO_CONN_STR")
    mongo_username = os.getenv("MONGO_USERNAME")
    mongo_password = os.getenv("MONGO_PASSWORD")
    
    max_retries = 5
    retry_delay = 5  # seconds

    for attempt in range(max_retries):
        try:
            print(f"Connecting to MongoDB with connection string: {mongo_conn_str}")
            client = AsyncIOMotorClient(mongo_conn_str)
            await client.admin.command('ismaster')  
            database_name = mongo_conn_str.split('/')[-1]
            database = client[database_name]
            print(f"Connected to database: {database_name}")
            return
        except Exception as e:
            print(f"Connection attempt {attempt + 1} failed: {str(e)}")
            if attempt < max_retries - 1:
                print(f"Retrying in {retry_delay} seconds...")
                await asyncio.sleep(retry_delay)
            else:
                print("Failed to connect to database after multiple attempts.")
                raise

def get_database():
    global database
    return database