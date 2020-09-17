from db import db

class PlaceModel(db.Model):
	__tablename__ = 'places'

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80))
	desc_sv = db.Column(db.String(3000))

	location_id = db.Column(db.Integer, db.ForeignKey('locations.id'))
	location = db.relationship('LocationModel')

	def __init__(self, name, desc_sv, location_id):
		self.name = name
		self.desc_sv = desc_sv
		self.location_id = location_id

	def json(self):
		return {'name': self.name, 'desc_sv': self.desc_sv}

	@classmethod
	def find_by_name(cls, name):
		return cls.query.filter_by(name=name).first()

	def save_to_db(self):
		db.session.add(self)
		db.session.commit()

	def delete_from_db(self):
		db.session.delete(self)
		db.session.commit()