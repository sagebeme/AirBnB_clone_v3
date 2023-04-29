#!/usr/bin/pyhton3

"""
Index file
"""

from api.v1.views import app_views
from flask import jsonify

@app_views.route('/status')
def status():
    """
    status: Status of API
    """
    return jsonify({"status":"OK"})
