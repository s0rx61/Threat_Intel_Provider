#Title: api
#API functionality

from flask import Flask, request
from flask_restful import Resource, Api
import ProviderDatabase


app = Flask(__name__)
api = Api(app)
#app.config["DEBUG"] = True

class select_table_by_number(Resource):
	def get(self, table_name, number):
		connection, cursor = ProviderDatabase.get_connection()
		return ProviderDatabase.select_table_by_number( connection, cursor, table_name, int(number))

class select_table_by_id(Resource):
	def get(self, table_name, id):
		connection, cursor = ProviderDatabase.get_connection()
		return ProviderDatabase.select_table_by_id( connection, cursor, table_name, id)

class select_table_by_hash(Resource):
	def get(self, table_name, type, hash):
		connection, cursor = ProviderDatabase.get_connection()
		return ProviderDatabase.select_table_by_hash( connection, cursor, type, hash, table_name)

class select_all_table(Resource):
	def get(self, table_name):
		connection, cursor = ProviderDatabase.get_connection()
		return ProviderDatabase.select_all_table( connection, cursor, table_name)

class select_table_by_date(Resource):
	def get(self, table_name, date):
		connection, cursor = ProviderDatabase.get_connection()
		return ProviderDatabase.select_table_by_date( connection, cursor, table_name, date)

class select_table_by_salesforce(Resource):
	def get(self, table_name):
		connection, cursor = ProviderDatabase.get_connection()
		return ProviderDatabase.select_table_by_salesforce( connection, cursor, limit)

#search table by number
api.add_resource(select_table_by_number, '/table/<table_name>/<number>')

#search table by Id
api.add_resource(select_table_by_id, '/id/<table_name>/<id>')

#search table by hash
api.add_resource(select_table_by_hash, '/hash/<type>/<hash>')

#download all the data by table
api.add_resource(select_all_table, '/table/all/<table_name>/')

#search table by date
api.add_resource(select_table_by_date, '/date/<table_name>/<date>' )

#search ip table by ip
api.add_resource()

#search by salesforce realted flag. ALso includes entry points
api.add_resource(select_table_by_salesforce, '/salesforce/<limit>')


if __name__ == '__main__':
	app.run()

