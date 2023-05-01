#!/usr/bin/pyhton3

"""
Index file
"""
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models import storage
from api.v1.views import app_views
from flask import jsonify, request


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """
    status: Status of API
    """
    if request.method == 'GET':
        resp ={"status":"OK"}
    return jsonify(resp)


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def get_stats():
    """
    endpoint: gets number of each objects by type
    """
    classes = [Amenity, City, Place, Review, State, User]
    names = ["amenity", "city", "place", "review", "states", "users"]

    if request.method == 'GET':
        num_obj = {}
        for i in range(len(classes)):
            num_obj[names[i]] = storage.count(classes[i])
        return jsonify(num_obj)
