from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps

db = create_engine("sqlite:///salaries.db") #close db?

app = Flask(__name__)
api = Api(app)

class departments(Resource):
    def get(self):
        conn = db.connect()
        query = conn.execute("select distinct DEPARTMENT from salaries")
        return {"departments": [i[0] for i in query.cursor.fetchall()]} #separate var and return that?

class departmentSalary(Resource):
    def get(self, departmentName):
        conn = db.connect()
        query = conn.execut("select * from salaries where Department = '{}'".format(departmentName.upper())
        result = {"data": [dict(zip(tuple (query.keys()), i)) for i in query.cursor]}
        return result

api.add_resource(departmentSalary, "/dept/<string:departmentName>")
api.add_resource(departments, "/departments")

if __name__ == "__main__":
    app.run()
