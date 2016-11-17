from flask import Flask, jsonify, request
import httplib
import ast
import requests
import json
from kazoo.client import KazooClient
from kazoo.client import KazooState
from kazoo.exceptions import KazooException
import logging

app = Flask(__name__)

@app.route('/forecast/json', methods = ['POST'])  #test commit
def forecast():
  result = ast.literal_eval(request.data)
  result["serviceId"] = "Forecast"
  kml_contents = ""
  headers = {'Content-Type': 'application/json'}
  parsed_json = {'result':'forecast_ran'}

  result["text"] = "KML generated"	
  print result
  r = requests.post("http://ec2-35-161-48-143.us-west-2.compute.amazonaws.com:8080/SG_MICROSERVICE_REGISTRY/gateway/message/saveData", data=json.dumps(result), headers=headers)  
  print r.status_code
  return jsonify(parsed_json)

def createConnection():
  zk = KazooClient(hosts='127.0.0.1:2181')
  zk.start()
  zk.add_listener(my_listener)
  print "tryin to create node"
  if zk.exists("/load-balancing-example"):
    print "----> node already exists"
  else:
    #Change this to refect dynamic ip and path
    zk.create("/my/favorite/node2",b"http://12.22.33.22:1209",ephemeral=True,makepath=True)

def tearDown():
  zk.stop()

def my_listener(state):
  if state == KazooState.LOST:
    # Register somewhere that the session was lost
    zk = KazooClient(hosts='127.0.0.1:2181')
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

connect()
