from database.database import Base, engine
from database.launch_model import LaunchRecord

# This will initalize and populate the database from api
def initialize_database():
    Base.metadata.create_all(engine)

if __name__ == "__main__":
    initialize_database()
    print("Database initialized successfullly.")
