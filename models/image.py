from db import db

class ImageModel(db.Model):
	__tablename__ = 'images'

	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String(250))

	place_id = db.Column(db.Integer, db.ForeignKey('places.id'))
	place = db.relationship('PlaceModel')

	def __init__(self, url, place_id):
		self.url = url
		self.place_id = place_id

	def json(self):
		return {'url': self.url}

	@classmethod
	def find_by_place(cls, _id):
		return cls.query.filter_by(place_id=place_id).all()

	@classmethod
	def find_by_id(cls, _id):
		return cls.query.filter_by(id=_id).first()

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()