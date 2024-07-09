from flask import jsonify, Blueprint

trips_routes__bp = Blueprint("trip_routes", __name__)

@trips_routes__bp.route("/trips", methods=["POST"])
def create_trip():
    return jsonify({"ola": "mundo"}), 200