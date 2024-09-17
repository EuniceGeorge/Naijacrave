# Naijacrave ~ *A web service for food enthusiast*

![food recipe](https://github.com/user-attachments/assets/f19d709b-8f94-4851-959e-3e0807162ef7)

# Table of Content
- [Introduction](#introduction)
    - [The Project](#the-project)
    - [The Context](#the-context)
    - [Author](#author)
- [API](#api)
- [Architecture](#architecture)
- [Future](#future)
- 
  
## Introduction

### The Project
Naijacrave is a web-based food service that helps users discover and manage recipes tailored to their available ingredients. It allows users to search for recipes, create or share their own, and log in to access personalized features.
The service is designed to simplify meal planning by providing recipe suggestions based on what users have at home, promoting convenience and minimizing food waste.

### The Context
This project is our Portfolio Project, concluding our Foundations Year at Holberton School.
We were able to choose who we wanted to work with and what we wanted to work on, as long as we present a working program at the end of the three weeks of development.

### Author
Eunice George is a former Strategist Information assistant and current full stack software engineer with a passion for providing technical solution for businesses and products that connect and empower others. 
<br> **Eunice George** https://github.com/EuniceGeorge- Virtual Assistant, Fashion Designer, Software Engineer.<br>

## API
I built an internal RESTful API for this web application so that data can be flexibly retreived from the MySQLdb. All available endpoints can be found in the api.app directory. Here's a description of the endpoint:

/api/recipes

* GET: Retrieves all recipes objects for a list of ingredients and returns a list of Recipes containing all the ingredients.
    
* POST: Creates recipe or share a recipe idea 

## Architecture

## Future
Beyond this initial MVP which was built in 3 weeks, I would like to continue to add many more features to the food recipe web service. In particular, I would like to setup an authentication system, such that when a user wants to share recipe, it will be checked if the recipe exist in the database or not before allowing it into the database. In addition, I'd like to allow users to search for recipe via category.

If you have any feedback (ex: feature ideas) or would like to contribute to this project, please feel free to contact me.
