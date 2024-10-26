from flask import Blueprint, request, jsonify
from src.calculators.calculator_1 import Calculator_1
from src.main.errors.error_controler import handle_errors

calc_routes_bp = Blueprint("calc_routes", __name__)

@calc_routes_bp.route("/calculator/1", methods=['POST'])
def calcultor_1():
   try:
      calc_1 = Calculator_1()
      response = calc_1.calculate(request)
      
      return jsonify(response)
   
   except Exception as exception:
      response = handle_errors(exception)
      return jsonify(response["body"]), response["status_code"]