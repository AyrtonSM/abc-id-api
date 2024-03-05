from utils.response_http_code import ResponseHttpCode
from flask import Blueprint, request, Response
from controller.luna_controller import LunaController
import logging as logger

luna_routes_controller_bp = Blueprint('luna_routes_controller', __name__)


class LunaRoutesController:
    @staticmethod
    @luna_routes_controller_bp.route("/")
    def index():
        return "Welcome to LUNA Api"

    @staticmethod
    @luna_routes_controller_bp.route("/prediction", methods=["POST"])
    def prediction():
        luna_controller = LunaController()
        logger.warning("-------->  %s", request.json)
        result = luna_controller.predict(request.json)
        response = Response()
        response.headers['Content-Type'] = 'application/json'

        if result is None:
            response.data = str({"message": "Sorry, something bad happened with the server"})
            response.status_code = ResponseHttpCode.SERVER_GENERAL_ERROR.value

            return response

        percentage = result * 100
        logger.warning("-------->  %s", percentage)

        if result > 0.8:
            message = f"Dear Physician, this person contains ::: {percentage:.2f}% of chance of containing a breast cancer. I recommend to start the treatment as soon as possible"
        else:
            message = f"Dear Physician, this person contains ::: {percentage:.2f}% of chance of containing a breast cancer."

        response.data = str({"message": message})
        response.status_code = 200

        return response
