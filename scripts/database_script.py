import os, sys, inspect
if "DOCKER_ENV" not in  os.environ:
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    parentdir = os.path.dirname(currentdir)
    # print(currentdir)
    # print(parentdir)
    sys.path.append(parentdir+"/data_gathering")
from database_manager import Database
import database_manager
from sqlalchemy import create_engine

if __name__ == "__main__":
    db = Database()
    database_manager.drop_database(db)
    db.get_session().commit()
    database_manager.create_database(db)
    db.get_session().commit()