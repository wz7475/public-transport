import json
import psycopg2

credentials_file = open("app/secrets.json")
credentials = json.load(credentials_file)
con = psycopg2.connect(
    host=credentials["host"],
    database=credentials["database"],
    user=credentials["user"],
    password=credentials["password"],
)

cur = con.cursor()
