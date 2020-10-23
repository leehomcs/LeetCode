#!/usr/bin/python3
from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db_connect = create_engine('sqlite:///users.db')
app = Flask(__name__)
api = Api(app)


class Users(Resource):
  def get(self):
    conn = db_connect.connect()  # connect to database
    query = conn.execute("select * from Users")  # This line performs query and returns json result
    return {'users': [i[0] for i in query.cursor.fetchall()]}  # Fetches first column that is Employee ID

class Add_A_User(Resource):
  def post(self, request):
    conn = db_connect.connect()
    print(request.json)
    UserId = request.json['UserId']
    LastName = request.json['LastName']
    FirstName = request.json['FirstName']
    Email = request.json['Email']
    Phone = request.json['Phone']
    Address = request.json['Address']
    Password = request.json['Password']
    Logtime = request.json['Logtime']
    query = conn.execute("insert into users values('{0}','{1}','{2}','{3}', \
                             '{4}','{5}, {6}, {7}')".format(UserId, LastName, FirstName, Email, Phone, Address, Password, Logtime))
    return {'status': 'success'}

class Del_a_User(Resource):
  def del_user(self, user_id):
    conn = db_connect.connect()
    query = conn.execute("delete from Users WHERE UserId = ?", user_id)
    return {'status': 'success'}

class Update_User_Email(Resource):
  def get(self, email, user_id):
    conn = db_connect.connect()
    query = conn.execute("update Users set Email = ? where UserId = ?", email)
    return {'status': 'success'}

class Get_A_User(Resource):
  def get(self, user_id):
    conn = db_connect.connect()
    query = conn.execute("select  UserId, LastName, FirstName, Email, Phone, Address from Users where UserId = ?", int(user_id))
    result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
    return jsonify(result)

class Get_Users(Resource):
  def get(self, location):
    conn = db_connect.connect()
    query = conn.execute("select  LastName, FirstName, Email, Phone, Address from Users where Address = ?", location)
    result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
    return jsonify(result)

class Update_User_Password(Resource):
  def get(self, user_id, new_pwd):
    conn = db_connect.connect()
    query = conn.execute("update Users set Password = ? where UserId = ?", (new_pwd, user_id))
    return {'status': 'success'}

class Get_User_by_Time(Resource):
  def get(self, log_time):
    conn = db_connect.connect()
    query = conn.execute("select  LastName, FirstName, Email, Phone, Address from  Users where  Logtime >= ?", log_time)
    return {'status': 'success'}


api.add_resource(Add_A_User, '/users/<request>')  # Route_1
api.add_resource(Del_a_User, '/users/<user_id>')  # Route_2
api.add_resource(Update_User_Email, '/users/<user_id>')  # Route_3
api.add_resource(Get_A_User, '/users/<user_id>')  # Route_2
api.add_resource(Get_Users, '/users/<location>')  # Route_3
api.add_resource(Update_User_Password, '/users/<user_id>&<password>')  # Route_2
api.add_resource(Get_User_by_Time, '/users/<log_time>')  # Route_3

if __name__ == '__main__':
  app.run()

# To prevent a massive amount of API requests that can cause a DDoS attack or other misuses of the API service,
# apply a limit to the number of requests in a given time interval for each API (also called spike arrest).
# When the rate is exceeded, block access from the API key at least temporarily,
# and return the 429 (too many requests) HTTP error code.