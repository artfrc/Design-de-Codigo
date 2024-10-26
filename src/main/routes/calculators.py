from flask import Blueprint, request, jsonify
from src.calculators.calculator_1 import Calculator_1

calc_routes_bp = Blueprint("calc_routes", __name__)

@calc_routes_bp.route("/calculator/1", methods=['POST'])
def calcultor_1():
   calc_1 = Calculator_1()
   response = calc_1.calculate(request)
   
   return jsonify(response)