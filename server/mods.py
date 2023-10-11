import json
from flask import jsonify
from models import Bakery
from app import app

with app.app_context():
    @app.route('/bakeries', methods=['GET'])
    def my_bakeries():
        my_bakeries = []

        # Query all bakeries from the database
        bakeries = Bakery.query.all()

        # Extract the names of the bakeries
        for bakery in bakeries:
            my_bakeries.append(bakery.name)

        # Return the list of bakery names as JSON
        return jsonify(my_bakeries)

if __name__ == '__main__':
    app.run(port=8080,debug=True)