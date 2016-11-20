from flask import Flask, jsonify, request
import httplib
import ast
import requests
import json
from kazoo.client import KazooClient
from kazoo.client import KazooState
from kazoo.exceptions import KazooException
import logging
import uuid
import calendar, datetime, time
from datetime import datetime

app = Flask(__name__)
ec2Ip=""
#ec2Ip = "127.0.0.1"
@app.route('/forecast/json', methods = ['POST'])  #test commit
def forecast():
  global ec2Ip
  result = ast.literal_eval(request.data)
  result["serviceId"] = "Forecast"
  kml_contents = ""
  headers = {'Content-Type': 'application/json'}
  parsed_json = {'result':'forecast_ran'}

  result["text"] = "KML generated"	
  print result
  r = requests.post("http://ec2-35-160-137-157.us-west-2.compute.amazonaws.com:8080/SG_MICROSERVICE_REGISTRY/gateway/message/saveData", data=json.dumps(result), headers=headers)  
  print r.status_code
  return jsonify(parsed_json)

def createConnection():
  global ec2Ip
  id = str(uuid.uuid4())
  hostIp = ec2Ip+":2181"
  zk = KazooClient(hosts=hostIp)
  zk.start()
  zk.add_listener(my_listener)
  path = "http://"+ec2Ip+":64000/forecast/json"
  print "tryin to create node"
  #zk.create("/load-balancing-example/forecast",hostIp,ephemeral=True,makepath=True)
  zk.create("/load-balancing-example/forecast/"+id, json.dumps({'name': 'forecast', 'id': id, 'address': ec2Ip, 'port': 64000,'sslPort': None, 'payload': None,'registrationTimeUTC': (datetime.utcnow() - datetime.utcfromtimestamp(0)).total_seconds(),'serviceType': 'DYNAMIC',"uriSpec": {"parts": [{"value": path, "variable": False}]}}, ensure_ascii=True).encode(),ephemeral=True,makepath=True)

def tearDown():
  zk.stop()

def my_listener(state):
  global ec2Ip
  if state == KazooState.LOST:
    # Register somewhere that the session was lost
    hostIp = ec2Ip+":2181"
    zk = KazooClient(hosts=hostIp)
    zk.start()

  elif state == KazooState.SUSPENDED:
    # Handle being disconnected from Zookeeper
    print "connection suspended"
  else:
    # Handle being connected/reconnected to Zookeeper
    print "connection error"

#@app.before_first_request
def connect():
  try:
    createConnection()
  except KazooException as e:
    print e.__doc__
    print "error "+e.message
  logging.basicConfig()

if __name__=='__main__':
  ec2Ip = requests.get("http://checkip.amazonaws.com/").text.split("\n")[0]
  print "global ec2Ip"+ec2Ip
  connect()
  app.run(debug=True, host = '0.0.0.0', port = 64000)


