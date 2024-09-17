# import os
from flask_sqlalchemy import SQLAlchemy
# from flask import Flask, render_template, request, url_for, redirect, jsonify
# from sqlalchemy import or_, Table, Column, Integer, ForeignKey
from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.sql import func
"""
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://naijacrave:crave@localhost/naijacrave'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
"""
class Base(DeclarativeBase):
    ...

db = SQLAlchemy(model_class=Base)

class Ingredient(db.Model):
    __tablename__ = 'ingredients'
    ingredient_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    ingredient_name = db.Column(db.String(255), unique=True, nullable=False)
    recipes = db.relationship('Recipe', secondary='ingredient_recipe',back_populates='ingredients')

class Recipe(db.Model):
    __tablename__ = 'recipes'
    recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_name = db.Column(db.String(255), unique=True, nullable=False)
    ingredients = db.relationship('Ingredient', secondary='ingredient_recipe', back_populates='recipes')
    #directions = db.relationship('Direction', back_populates='recipe')
    directions = db.Column(db.Text, nullable=False)

class IngredientRecipe(db.Model):
    __tablename__ = 'ingredient_recipe'
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipes.recipe_id'), primary_key=True)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredients.ingredient_id'), primary_key=True)

"""class Direction(db.Model):
    __tablename__ = 'directions'
    direction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey('recipe.recipe_id'), nullable=False)
    recipe = db.relationship('Recipe', back_populates='directions')

    def to_dict(self):
        return {
                "direction_id": self.direction_id,
                "recipe_id": self.recipe_id,
                "direction": self.direction
                }
"""
# if __name__ == '__main__':
#     with app.app_context():
#         main_menu()
