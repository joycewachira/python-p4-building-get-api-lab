#!/usr/bin/env python3

from flask import Flask, make_response, jsonify,json
from flask_migrate import Migrate

from models import db, Bakery, BakedGood

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Bakery GET API</h1>'

@app.route('/bakeries')
def bakeries():
  
   my_bakery=[]    
   for bakery in Bakery.query.all():
       my_dict={
           "name":bakery.name,
           "created_at":bakery.created_at,
           "updated_at":bakery.updated_at 
       }
       my_bakery.append(my_dict)
   response =make_response(jsonify(my_dict),200)
   response.headers["Content-Type"]="application/json"

   return response
      
       

#    bakeries.to_dict()
#    response =make_response(jsonify(bakeries))
      


@app.route('/bakeries/<int:id>')
def bakery_by_id(id):
    bakery =Bakery.query.filter(Bakery.id==id).first()
    mybakery_Dict=bakery.to_dict()
    response =make_response(jsonify(mybakery_Dict),200)
    response.headers["Content-Type"]="application/json" 
    return response

@app.route('/baked_goods/by_price')
def baked_goods_by_price():
    baked_goods=BakedGood.query.order_by(BakedGood.price.desc()).all()
    my_baked_goods_list =[]
    for baked in baked_goods:
        baked_goods_json={
                'name': baked.name,
                'price': baked.price,
                'bakery_id': baked.bakery_id,
                'created_at': baked.created_at,
                'updated_at': baked.updated_at
            }
        my_baked_goods_list.append(baked_goods_json)
    response =make_response(jsonify(baked_goods_json),200)
    
    return response

@app.route('/baked_goods/most_expensive')
def most_expensive_baked_good():
    most_expensive_baked_good = BakedGood.query.order_by(BakedGood.price.desc()).first()
    if most_expensive_baked_good:
        # Serialize the most expensive baked good into JSON
        baked_good_json = {
            'id': most_expensive_baked_good.id,
            'name': most_expensive_baked_good.name,
            'price': most_expensive_baked_good.price,
            'bakery_id': most_expensive_baked_good.bakery_id,
            'created_at': most_expensive_baked_good.created_at,
            'updated_at': most_expensive_baked_good.updated_at
        }

        # Return the most expensive baked good as JSON
        return make_response(jsonify(baked_good_json),200)
    else:
        # Handle the case where no baked goods are found
        return jsonify({'message': 'No baked goods found'}), 404



  

if __name__ == '__main__':
    app.run(port=5555, debug=True)
