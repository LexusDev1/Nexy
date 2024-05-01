from lib.util.database import DB

# Create an instance of the DB class
db = DB()
print(db)

# Connect to the database
db.connect("your_host", 27017)  # Replace "your_host" with your MongoDB host address

# Get a reference to the database
if db:
  database = db.get_database("your_database_name")# Replace "your_database_name" with your database name
  print(database)

hi = db.create_database("my_database")
print(hi)