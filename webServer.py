from functools import partial
from flask import Flask, request
from flask_restful import Api, Resource
from datetime import datetime as time
import requests
import sys


app = Flask(__name__)
api = Api(app)


HOST = f'http://{sys.argv[1]}:5000'
# HOST = "http://10.8.0.14:5000"

class Tarefas(Resource):
   

    def getTime(self):
        return time.now.strftime("%d/%m/%Y - %H:%M:%S")

    def get(self):
        res = requests.get(HOST + "/Tarefa")
        return res.text, 200

    def post(self):
        taskName = request.json["taskName"]
        res = requests.post(HOST + "/Tarefa", json = {"taskName": taskName})
        return res.text, 200


class tarefaAPI(Resource):
    def getTime(self):
        return time.now.strftime("%d/%m/%Y - %H:%M:%S")

    def get(self, id):
        res = requests.get(HOST + "/Tarefa/" + str(id))
        return res.text, 200

    def put(self, id):
        updatedTask = request.json["updatedTask"]
        res = requests.put(HOST + "/Tarefa/" + str(id), json = {"updatedTask": updatedTask})
        return res.text, 200

    def delete(self, id):
        res = requests.delete(HOST + "/Tarefa/" + str(id))
        return res.text, 200


class healthCheck(Resource):
    def get(self):
        return 200

class healthCheck_priv(Resource):
    def get(self):
        res = requests.delete(HOST + "/healthcheck")
        return 200


if __name__ == '__main__':
    api.add_resource(Tarefas, '/Tarefa', endpoint='tarefas')
    api.add_resource(tarefaAPI, '/Tarefa/<int:id>', endpoint='tarefa')
    api.add_resource(healthCheck, '/healthcheck', endpoint='healthcheck')
    api.add_resource(healthCheck_priv, '/healthcheck-priv', endpoint='healthcheck-priv')


    app.run(host='0.0.0.0', debug=True)

