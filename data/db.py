import psycopg2
import os
from dotenv import load_dotenv

# Load .env variables (adjust path if needed)
load_dotenv()

def fetch_contacts():
    conn = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )
    cur = conn.cursor()
    cur.execute("SELECT name, email, password FROM Qspider_Pytest")
    rows = cur.fetchall()  #  Only call once
    cur.close()
    conn.close()
    return rows  #  List of tuples

