#!/usr/bin/python3
"""This module instantiates an object of class FileStorage"""
import os


storage_type = os.getenv('HBNB_TYPE_STORAGE', None)
db = os.getenv('HBNB_MYSQL_DB', None)
print(f'storage_type -> {storage_type} & db -> {db}')
if (storage_type and storage_type == 'db'):
    print('using db_storage')
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    print('using file_storage')
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
storage.reload()
