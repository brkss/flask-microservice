import os 


user = os.getenv('MYSQL_USER')
password = os.getenv('MYSQL_PASSWORD')
host = os.getenv('MYSQL_HoST')
db = os.getenv('MYSQL_DB')
port = os.getenv('MYSQL_PORT')

DB_CONNECTION_URI = f'mysql://{user}:{password}@{host}:{port}/{db}'

