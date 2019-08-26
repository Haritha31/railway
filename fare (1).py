from flask import Flask
from flask import request
from flask import make_response
import json
import requests

#flask set up
app = Flask(__name__)
@app.route('/fare', methods=["GET","POST"])
def fare():
    req = request.get_json(silent=True, force=True)
    no = req["queryResult"]["parameters"]["number"]
    source=req["queryResult"]["parameters"]["source"]
    dest=req["queryResult"]["parameters"]["destination"]
    quota=req["queryResult"]["parameters"]["quota"]
    action=req["queryResult"]["action"]
    #base_url='http://indianrailapi.com/api/v2/TrainFare/apikey/f0b655638770e7ffc18f1dcef0385648/TrainNumber/'
    response=requests.get("http://indianrailapi.com/api/v2/TrainFare/apikey/52d75214a37987fd7ab582c149e43b77/TrainNumber/12565/From/SEE/To/NDLS/Quota/"+quota).json()

    c=len(response["Fares"])
    for i in range(c):
        if(response["queryResult"][i]["quota"]==quota):
            fare=response["queryResult"][i]["Fare"]
            break
    return train(fare, action)

def train(fare,action):
    if action=="TextResponse":
        return {
            "fulfillment": "The fare is "+str(fare)
        }


if __name__ == '__main__':
    app.run(port=3000,debug=True)