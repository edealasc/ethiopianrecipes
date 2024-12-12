from flask import Flask, jsonify, request
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

# Corrected: Open the file and load the JSON data
with open(r'rest api\recipes.json', 'r') as file:
    recipe_data = json.load(file)

class Recipe(Resource):
    def get(self):
        return recipe_data
    
class RecipeId(Resource):
    def get(self, recipe_id):
        return recipe_data[recipe_id]

class RecipeSearch(Resource):
    def get(self, search_query):
        search_results = []

        # Search by title
        for r in recipe_data:
            if search_query.lower() in r["title"].lower():
                search_results.append(r)

        # Search by ingredients
        for r in recipe_data:
            for ingredient in r.get("ingredients", []):
                if isinstance(ingredient, dict):
                    # Handle dictionary ingredients
                    ingredient_value = ingredient.get("name", "")  # Default to empty string if "name" not found
                    if search_query.lower() in ingredient_value.lower():
                        search_results.append(r)
                        break
                elif isinstance(ingredient, str):
                    # Handle string ingredients
                    if search_query.lower() in ingredient.lower():
                        search_results.append(r)
                        break

        # Search by instructions
        for r in recipe_data:
            for instruction in r.get("instructions", []):
                if isinstance(instruction, dict):
                    if search_query.lower() in instruction.get("step", "").lower():
                        search_results.append(r)
                        break
                elif isinstance(instruction, str):
                    if search_query.lower() in instruction.lower():
                        search_results.append(r)
                        break

        return search_results

class NotFound(Resource):
    def get(self):
        return "Resource not found!"

api.add_resource(Recipe,'/recipes')
api.add_resource(RecipeId,'/recipe/<int:recipe_id>')
api.add_resource(RecipeSearch,'/recipes/<string:search_query>')
api.add_resource(NotFound,'/<path:path>')

if __name__ == "__main__":
    app.run(debug=True)