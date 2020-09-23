from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
from models.place import PlaceModel

class Place(Resource):
	parser = reqparse.RequestParser()
	parser.add_argument('desc_sv',
		type=str,
		required=True,
		help="This field cannot be left blank!")

	parser.add_argument('location_id',
		type=int,
		required=True,
		help="Every place needs a location.")

	def get(self, name):
		place = PlaceModel.find_by_name(name)
		if place:
			return place.json()
		return {'message': 'Place not found'}, 404


	#@jwt_required()
	def post(self, name):
		if PlaceModel.find_by_name(name):
			return {'message': "A place with name '{}' already exists.".format(name)}, 400

		data = Place.parser.parse_args()
		place = PlaceModel(name, data['desc_sv'], data['desc_en'], data['desc_de'], data['lat'], data['lon'], data['location_id'])
		
		print(place.name)
		print(place.desc_sv)
		try:
			place.save_to_db()
		except:
			return {'message': 'An error occured inserting the place'}, 500

		return place.json(), 201

	def delete(self, name):
		place = PlaceModel.find_by_name(place)
		if place:
			place.delete_from_db()

	def put(self, name):
		data = Place.parser.parse_args()

		place = PlaceModel.find_by_name(name)

		if place is None:
			place = PlaceModel(name, **data)
		else:
			place.desc_sv = data['desc_sv']

		place.save_to_db()
		return place.json()


class PlaceList(Resource):
	def get(self):
		return {'places': [place.json() for place in PlaceModel.query.all()]}