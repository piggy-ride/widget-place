import mysql.connector
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

host = os.getenv("host")
user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("database")

connection = mysql.connector.connect(
    host=host,
    user= user,
    password =password,
    database=database
)

cursor = connection.cursor