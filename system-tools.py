import sys
import os
import time
import requests
import redis

from flask import Flask, request
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)
redis_db = redis.StrictRedis(host=str(os.environ['REDIS_SERVICE_HOST']), port=str(os.environ['REDIS_SERVICE_PORT']))

class SystemToolTime(Resource):
    def get(self):
        ## SYSTEM_TIME is the name of the subscribed microservice that is been onboarded.
        ## The subscribed microservice should always be provided in caps while fetching from redis db.
        ms_json = eval(redis_db.get('SYSTEM-TIME'))
        ## 10002 is the port on which the subscibed microservice "system-time" is running.
        url = str(ms_json["10002"])
        headers = {            
            'API-KEY': redis_db.get('API-KEY')
            }
        resp = requests.request("GET", url, headers=headers)
        #resp = requests.get(url)
        return resp.json()


class SystemToolUpTime(Resource):
    def get(self):
        ## SYSTEM_UPTIME is the name of the subscribed microservice that is been onboarded.
        ## The subscribed microservice should always be provided in caps while fetching from redis db.
        ms_json = eval(redis_db.get('SYSTEM-UPTIME'))
        ## 10004 is the port on which the subscibed microservice "system-uptime" is running.
        url = str(ms_json["10004"])
        headers = {            
            'API-KEY': redis_db.get('API-KEY')
            }
        resp = requests.request("GET", url, headers=headers)
        #resp = requests.get(url)
        return resp.json()


api.add_resource(SystemToolTime, '/systemtoolstime')
api.add_resource(SystemToolUpTime, '/systemtoolsuptime')


if __name__ == '__main__':
    if(len(sys.argv) > 1):
        run_port = sys.argv[1]
    else:
        run_port = 10000
    
    app.run(host='0.0.0.0',port=int(run_port), debug=True)
