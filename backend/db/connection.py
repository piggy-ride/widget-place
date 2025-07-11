import mysql.connector
import os
from dotenv import find_dotenv, load_dotenv

dotenv_path = find_dotenv()

load_dotenv(dotenv_path)

user = os.getenv("user")
password = os.getenv("password")
database = os.getenv("database")

connection = mysql.connector.connect(
    host="localhost",
    user= user,
    password =password,
    database=database
)

cursor = connection.cursor