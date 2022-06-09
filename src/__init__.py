import os, sys
from .database import DataBase


sys.path.append(os.path.dirname(os.path.realpath(__file__)))

print(os.getcwd())

db = DataBase()