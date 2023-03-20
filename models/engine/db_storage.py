#!/usr/bin/python3

import sqlalchemy
from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import sessionmaker
from models.base_model import BaseModel, Base
import os


class DBStorage:
    __engine = None
    __session = None

    def __init__(self):
        user = os.getenv('HBNB_MYSQL_USER')
        pwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        db = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, pwd, host, db), pool_pre_ping=True)

        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        metadata = MetaData(bind=self.__engine)

        if os.getenv('HBNB_ENV') == "test":
            metadata.reflect(bind=self.__engine)
            metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        new_dict = {}
        # print(cls)
        if cls != None:
            all_obj = self.__session.query(cls).fetchall()
        else:
            all_obj = self.__session.query().fetchall()
        for obj in all_obj:
            index = obj.to_dict()['__class__'] + '.' + obj.id
            new_dict[index] = obj
        return new_dict
