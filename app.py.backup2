import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, Table, Column, Integer, ForeignKey
from flask_cors import CORS
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db_model import db, Ingredient, Recipe, IngredientRecipe, Direction
app = Flask(__name__)
CORS(app)
#mysql://username:password@host:port/database_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://naijacrave:crave@localhost/naijacrave'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)
db.init_app(app)

@app.route('/')
def home():
    return '<h1> Hello </h1>'

@app.route('/api/recipes', methods=['POST'])
def add_recipe():
    print("sdsd")
    data = request.get_json()

    recipe_name = data.get('recipe_name')
    ingredients = data.get('ingredients')
    directions = str(data.get('directions'))

    recp = db.session.query(Recipe).filter_by(recipe_name=recipe_name).first()
    if recp:
        return jsonify({"message": "A recipe with thesame name already exist"}), 409

    new_recipe = Recipe(recipe_name=recipe_name)
    db.session.add(new_recipe)
    db.session.commit()

    recipe_id = new_recipe.recipe_id
    
    for ing in ingredients:
        ingredient = db.session.query(Ingredient).filter_by(ingredient_name=ing).first()
        if ingredient:
            ing_id = ingredient.ingredient_id

        else:
            new_ing = Ingredient(ingredient_name=ing)
            db.session.add(new_ing)
            db.session.commit()

            ing_id = new_ing.ingredient_id
        
        new_ing_recipe = IngredientRecipe(recipe_id=recipe_id, ingredient_id=ing_id)
        db.session.add(new_ing_recipe)
        db.session.commit()

    new_direction = Direction(recipe_id=recipe_id, direction=directions)
    db.session.add(new_direction)
    db.session.commit()

    return jsonify({"message": "successfully added"}), 201

"""
#get all recipes
@app.route('/api/recipes', methods=['GET'])
def get_recipe():
    all_recipes = Recipe.query.all()

    if all_recipes:
        direction_list = [direction.to_dict() for direction in Recipe.directions]
        return jsonify({
            "recipe_id": recipe.recipe_id,
            "recipe_name": recipe.recipe_name,
            "directions": direction_list,
            "ingredients": [{"id": ing.ingredient_id, "ingredient_name": ing.ingredient_name} for ing in all_recipe.ingredients]
            })
    else:       
        return jsonify({"message": "Recipe not found"}), 404

"""
if __name__ == '__main__':
    app.run(debug=True)
