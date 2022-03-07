import os

from pymongo import MongoClient
from common.consts import *

mongo_client = MongoClient(os.environ.get("DB"))
configurations_db = mongo_client.configs
configurations_coll = configurations_db.orders


def save_request_data(req_body):
    document = {}
    document.update({CAPACITY_OPTION_KEY: req_body.get("capacity")})
    document.update({WHEELS_OPTION_KEY: req_body.get("wheels")})
    document.update({TIRES_OPTION_KEY: req_body.get("tires")})
    document.update({"name": req_body.get("name")})
    configurations_coll.insert_one(document)


def count_requests():
    return configurations_coll.count_documents({})
