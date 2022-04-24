
from distutils.debug import DEBUG
from distutils.log import INFO
import json
import os
import logging

from flask import Flask, jsonify, request
app = Flask(__name__)

#---------------------------------------------------------
# Basic route to get status of the pcloud solution.
# Status should check the database and rest servies and
# provide an ok for each
#---------------------------------------------------------

@app.route('/status')

def status():
    return jsonify({'status': 'ok'})

#---------------------------------------------------------
# Route to post a heartbeat to pcloud
#---------------------------------------------------------
@app.route('/currentWord',  methods=['GET'])

def currentWord():
    return jsonify({'status': "OK"},{'word':"today"})

#---------------------------------------------------------
# Run the REST API server
#---------------------------------------------------------
app.run()



