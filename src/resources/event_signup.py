from flask import request
from flask_restful import Resource
from http import HTTPStatus


class EventSignupResource(Resource):

    def put(self, email):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish = True

        return {}, HTTPStatus.NO_CONTENT

    def delete(self, email):
        recipe = next((recipe for recipe in recipe_list if recipe.id == recipe_id), None)

        if recipe is None:
            return {'message': 'recipe not found'}, HTTPStatus.NOT_FOUND

        recipe.is_publish = False

        return {}, HTTPStatus.NO_CONTENT
