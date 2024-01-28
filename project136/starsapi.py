from flask import Flask, jsonify, request
from data import data

app = Flask(__name__)

# @app.route("/")
# def index():
#     return jsonify({
#         "data": data,
#         "message": "success"
#     }), 200



@app.route("/star/<star_name>")
# <star_names> is placeholder for the name of a star. E.g. Sun
def star(star_name):
    # Try to find the data with the specified name
    star_data = next((item for item in data if item.get("star_name") == star_name), None)
    return jsonify({
        "data": star_data,
        "message": "success"
    }), 200
# you should access http://127.0.0.1:5000/star to reach the /star endpoint.

# Here, the name variable is used to retrieve the value of the "name" query parameter from the URL. For example, if the URL is http://127.0.0.1:5000/star?name=Sun, request.args.get("name") will return "Sun", and the code will look for a star with the name "Sun" in the data list.

# Note: In the later example where a dynamic parameter is used in the route (@app.route("/star/<star_name>")), there is no need to use request.args.get() because the value is directly extracted from the URL as a part of the route parameter.


if __name__ == "__main__":
    app.run()