import os
from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_, Table, Column, Integer, ForeignKey
from flask_cors import CORS
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from db_model import db, Ingredient, Recipe, IngredientRecipe
app = Flask(__name__)
CORS(app)
#mysql://username:password@host:port/database_name
#app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://naijacrave:crave@localhost/naijacrave'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://naijacrave:crave@localhost/naijacravedb2'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#db = SQLAlchemy(app)
db.init_app(app)

@app.route('/')
def home():
    return '<h1> Hello, man </h1>'

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

    new_recipe = Recipe(recipe_name=recipe_name, directions=directions)
    db.session.add(new_recipe)
    db.session.commit()

    recipe_id = new_recipe.recipe_id
    
    for ing in ingredients: #for all the ingredients entered in the ingredients list from the input
        ingredient = db.session.query(Ingredient).filter_by(ingredient_name=ing).first()#query the schema
        if ingredient: #if the ingredient is same as an ingredient in the database model 
            ing_id = ingredient.ingredient_id #assign the ingredient_id to the the variable ingredient and save it.

        else: # if the ingredient doesnt exit
            new_ing = Ingredient(ingredient_name=ing) # create a a new id for the ingredient
            db.session.add(new_ing)
            db.session.commit()

            ing_id = new_ing.ingredient_id #same as above for the new ingredient
        
        #assign the ingredient id and recipe id to new_ing_recipe
        new_ing_recipe = IngredientRecipe(recipe_id=recipe_id, ingredient_id=ing_id)
        db.session.add(new_ing_recipe)
        db.session.commit()
    return jsonify({"message": "successfully added"}), 201
"""  
    new_direction = Direction(recipe_id=recipe_id, direction=directions)
    db.session.add(new_direction)
    db.session.commit()
"""

#get all recipes
@app.route('/api/recipes', methods=['GET'])
def get_recipe():
    data = request.args.get('ingredients')
    if data:
        ingredients_list = data.split('%')

        ing_recp = db.session.query(Recipe).filter(Recipe.ingredients.any(Ingredient.ingredient_name.in_(ingredients_list))).all()

        if len(ing_recp) == 0:
            return jsonify({"message": "No recipes with these ingredients"}), 404

       # print(ing_recp)
        recipes = []
        for reci in ing_recp:
            tmp = {
                    'recipe_name': reci.recipe_name,
                    'recipe_id': reci.recipe_id,
                    'ingredients': [i.ingredient_name for i in reci.ingredients],
                    'directions': reci.directions
            }
            recipes.append(tmp)
           # print(reci.recipe_name)
        return jsonify(recipes)
    
    
    return jsonify({"message": "No parameter found"})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
