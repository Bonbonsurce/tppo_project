DEBUG = False
TESTING = False
LOG_FILE = "/home/filya/TPPO2/imit/logs/imit.log"
#SQLITE_DATABASE_PATH = "//path/to/sqlitedb/imit.db"
MYSQL_USER = "root"
MYSQL_PASSWORD = "Timit2!0"
MYSQL_HOST = "localhost"
MYSQL_DATABASE = "imit2"
#SQLALCHEMY_DATABASE_URI = "sqlite://" + SQLITE_DATABASE_PATH
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://{}:{}@{}/{}".format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_HOST, MYSQL_DATABASE)
