# -*- coding: utf-8 -*-
# time: 2020/3/5 上午10:46
from flask_restful import Resource, Api
from flask.blueprints import Blueprint

common_bp = Blueprint("common", __name__, url_prefix="/api/v1/common")

common_api = Api(common_bp)


@common_api.resource("/test")
class Common(Resource):

    def get(self):
        return {"hello": "world"}
