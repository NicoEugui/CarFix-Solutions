from dotenv import load_dotenv
import os
import psycopg2

# Cargar .env
load_dotenv()

def get_connection():
    try:
        return psycopg2.connect(
            database=os.getenv('DB_NAME'), 
            user=os.getenv('DB_USER'),  
            host=os.getenv('DB_HOST'),
            password=os.getenv('DB_PASSWORD'),
            port=os.getenv('DB_PORT'),
        )
    except Exception as e:
        print(e)

get_connection()
