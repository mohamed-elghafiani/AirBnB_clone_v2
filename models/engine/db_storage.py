#!/usr/bin/python3
"""DB Storage Module"""
from sqlalchemy import (create_engine)
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
import os


class DBStorage():
    """DB Storage class"""
    __engine = None
    __session = None

    def __init__(self):
        """Instance initiator"""
        db_user = os.environ.get("HBNB_MYSQL_USER")
        db_passwd = os.environ.get("HBNB_MYSQL_PWD")
        db_host = os.environ.get("HBNB_MYSQL_HOST")
        db_name = os.environ.get("HBNB_MYSQL_DB")
        env = os.environ.get("HBNB_ENV")

        self.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    db_user,
                    db_passwd,
                    db_host,
                    db_name
                ),
                pool_pre_ping=True
        )

        if env == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Query dababase session by cls"""
        results = {}

        if cls is None:
            classes = [User, State, City]
            for class_ in classes:
                objs = self.__session.query(class_).all()
                for obj in objs:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    results[key] = obj

        else:
            if type(cls) is str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(type(obj).__name__, obj.id)
                results[key] = obj

        return results

    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        if self.__session:
            self.__session.commit()

    def delete(self, obj=None):
        """"delete from the current database"""
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables of the database + the session"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place, place_amenity
        from models.amenity import Amenity

        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()

    def destroy(self):
        """drops all database tables"""
        Base.metadata.drop_all(self.__engine)

    def close(self):
        """call close() method on the private session attribute"""
        self.__session.close()
