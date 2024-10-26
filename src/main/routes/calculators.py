from flask import Blueprint, request, jsonify
from src.main.errors.error_controler import handle_errors
from src.main.factories.calculator_1_factory import Calculator_1_factory
from src.main.factories.calculator_2_factory import Calculator_2_factory
from src.main.factories.calculator_3_factory import Calculator_3_factory

calc_routes_bp = Blueprint("calc_routes", __name__)

@calc_routes_bp.route("/calculator/1", methods=['POST'])
def calcultor_1():
   try:
      calc_1 = Calculator_1_factory()
      response = calc_1.calculate(request)
      
      return jsonify(response)
   
   except Exception as exception:
      response = handle_errors(exception)
      return jsonify(response["body"]), response["status_code"]
   
   
@calc_routes_bp.route("/calculator/2", methods=['POST'])
def calcultor_2():
   try:
      calc_2 = Calculator_2_factory()
      response = calc_2.calculate(request)
      
      return jsonify(response)
   
   except Exception as exception:
      response = handle_errors(exception)
      return jsonify(response["body"]), response["status_code"]
   
@calc_routes_bp.route("/calculator/3", methods=['POST'])
def calcultor_3():
   try:
      calc_3 = Calculator_3_factory()
      response = calc_3.calculate(request)
      
      return jsonify(response)
   
   except Exception as exception:
      response = handle_errors(exception)
      return jsonify(response["body"]), response["status_code"]