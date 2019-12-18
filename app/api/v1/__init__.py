# -*- coding:utf-8 -*-
from flask import Blueprint
from app.api.v1 import db_main


def create_blueprint_v1():
    bp_v1 = Blueprint('v1', __name__)
    db_main.api.register(bp_v1)
    return bp_v1
