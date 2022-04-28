># Consuming temperature readings from IoT LoRa Temperature sensors

## Solutions within this repo:
### 1) Use of webhook with The Things Network (TTN)
### 2) Use of websockets with the LORIOT network

<br>

>## TTN webhook

## Introduction
This is a simple flask app that is an http endpoint for a webhook set up to run from an application setup on The Things Network (TTN).  

## Files
- webhook.py

## Required
- Flask.  Install with command
`
pip3 install Flask
`
- Gateways and temperature sensor end devices set up on TTN 

## Setup
Once logged into the TTN console (from here https://www.thethingsnetwork.org/), navigate to your applications and select the required application.  There select from the left hand menu 'integrations' and select 'Webhooks'.  Follow the instructions to set up and note the parameters below.

A webhook was added with the following parameters:

- Webhook ID: flaskapp-webhook
- Webhook format: JSON
- Base URL: The url of the webpage when application run (for instance: https://5000-cundritz-aggoraiotpoc-h4xw57hsrec.ws-eu34xl.gitpod.io/)
- Uplink message - Enabled with value '/webhook'

This then allowed for the JSON data to be read by the app in a dictionary format where it could be queried to provide the value of the required variables.

## Run the application
- type into the the console: 
`
python3 webhook.py
`

<br>

>## LORIOT WebSocket
## Introduction
This is a python app that is an WS endpoint for a websocket set up to run from an application setup on LORIOT network.  

## Files
- websocket.py

## Required
- websockets library.  Install with command
`
pip install websockets
`
- Gateways and temperature sensor end devices set up on LORIOT network

## Setup
Once logged into the LORIOT console (from here https://loriot.io/login.html), navigate to applications and select the required application.  From there select from the left hand menu 'Output' and click on 'Add new output' and select 'Websocket' as output.  Select the Websocket now listed under Output and note the instructions displayed on the right under 'Output Confiuguration' 

The target URL Template needs to added as the url variable value with the websocket.py file

The string object received by the websocket is converted to JSON to be read by the app in a dictionary format where it could be queried to provide the value of the required variables.  The hexidecimal encoded environment data is then passed to the decoder function to produce a python dictionary containing the temperature and humidity in a readable format.

## Run the application
- type into the the console: 
`
python3 websocket.py
`

<br>

>## Reference material.
### For the webhook:
- https://www.youtube.com/watch?v=X-_25tzo8Cw
- https://www.youtube.com/watch?v=HQLRPWi2SeA
- https://www.thethingsnetwork.org/docs/
### For the websocket:
- https://www.youtube.com/watch?v=tgtb9iucOts
- https://websockets.readthedocs.io/en/stable/index.html
- The data recieved from the uplink is a string.  To convert it to JSON the json.loads function was used as per the instructions here: https://stackoverflow.com/questions/988228/convert-a-string-representation-of-a-dictionary-to-a-dictionary
### For the decoder:
The decoder code was coverted from the JavaScript found in the below github repo directed from the Milesight support pages:
https://github.com/Milesight-IoT/SensorDecoders/tree/master/EM300_Series/EM300-TH


