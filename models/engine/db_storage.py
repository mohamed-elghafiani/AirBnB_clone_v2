#!/usr/bin/python3
"""DB Storage Module"""
from sqlalchemy.orm import scoped_session
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from models.base_model import Base, BaseModel


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

        if os.environ.get("HBNB_ENV") == "test":
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

        DBStorage.__engine = create_engine(
                'mysql+mysqldb://{}:{}@{}/{}'.format(
                    db_user,
                    db_passwd,
                    db_host,
                    db_name
                ),
                pool_pre_ping=True
        )

    def all(self, cls=None):
        """Query dababase session by cls"""
        results = {}
        classes = [User, State, City, Amenity, Place, Review]

        if cls is None:
            for class_ in classes:
                objs = self.__session.query(class_).all()
                for obj in objs:
                    key = "{}.{}".format(obj.__class__.__name__, obj.id)
                    results[key] = obj

        else:
            objs = self.__session.query(cls).all()
            for obj in objs:
                key = "{}.{}".format(type(cls).__class__, obj.id)


    def new(self, obj):
        """add the object to the current database session"""
        if obj:
            self.__session(obj)

    def save(self):
        """commit all changes of the current database session"""
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
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit)
        Session = scoped_session(session)
        self.__session = Session()

