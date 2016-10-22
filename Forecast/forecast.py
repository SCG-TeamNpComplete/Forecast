from flask import Flask, jsonify, request
import httplib
import ast
import requests
import json


app = Flask(__name__)

@app.route('/forecast/json', methods = ['POST'])  #test commit
def forecast():
  result = ast.literal_eval(request.data)
  result["serviceId"] = "Forecast"
  kml_contents = ""

  headers = {'Content-Type': 'application/json'}


  parsed_json = {'result':'forecast_ran'}


  #kml_file = open("KML_Samples.kml")


  result["text"] = "KML generated"	
  print result
  r = requests.post("http://ec2-35-161-48-143.us-west-2.compute.amazonaws.com:8080/SG_MICROSERVICE_REGISTRY/gateway/message/saveData", data=json.dumps(result), headers=headers)  
  print r.status_code
  return jsonify(parsed_json)
