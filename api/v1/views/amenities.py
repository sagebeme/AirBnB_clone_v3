#!/bin/python3

"""
    Amenities view model that handles,
    Restful Api action
"""

from models.amenity import Amenity
from models import storage
from api.v1.views import app_views
from flask import abort, jsonify, request


@app_view.route('/amenities', methods=['GET'], strict_slashes=False)
def get_amenities():
    """
    Purpose: Gets a list of all amenities
    """
    all_amenities = storage.all(Amenity).values()
    list_amenities = []
    for amenity in all_amenities:
        list_amenities.append(amenity.to_dict())
    return jsonify(list_amenities)


@app_views.route('/amenities/<amenity_id>', methods=['GET'],
                 strict_slashes=False)
def get_amenities(amenity_id):
    """
    Purpose: Gets an amenity
    """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    return jsonify(amenity.to_dict())


@app_views.route('/amenities/<amenity_id>', methods=['DELETE'],
                 strict_slashes=False)
def delete_amenity(amenity_id):
    """ Deletes a Amenity object """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    storage.delete(amenity)
    storage.save()
    return jsonify({}), 200


@app_views.route('/amenities', methods=['POST'], strict_slashes=False)
def post_amenity():
    """
    Creates a Amenity
    """
    if not request.get_json:
        abort(400, 'Not a JSON')

    if 'name' not in request.json:
        abort(400, 'Missing name')

    amenity = Amenity(**request.get_json())
    amenity.save()
    return jsonify(amenity.to_dict()), 201


@app_views.route('/amenities/<amenity_id>', methods=['PUT'],
                 strict_slashes=False)
def put_amenity(amenity_id):
    """
    Updates a Amenity object
    """
    amenity = storage.get(Amenity, amenity_id)
    if amenity is None:
        abort(404)

    if not request.json:
        abort(400, 'Not a JSON')
    ignore = ['id', 'created_at', 'updated_at']
    for key, value in request.get_json().items():
        if key not in ignore:
            setattr(amenity, key, value)
    amenity.save()
    return jsonify(amenity.to_dict()), 200

