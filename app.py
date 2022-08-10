from flask import Flask, jsonify, request, Response, make_response
from collections import Counter
import collections
import json
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId

app = Flask(__name__)

app.config[
    "MONGO_URI"
] = "mongodb+srv://OtterFox:1XTQqHNw9X7XvkXs@cluster0.uwltrza.mongodb.net/mineria"

mongo = PyMongo(app)

#Este metodo recupera todas las recetas disponibles
@app.route("/recipetwy", methods=["GET"])
def get_recipestwy():
    headers = {"Content-Type": "application/json"}
    recipes = mongo.db.recipes.find()
    response = json_util.dumps(recipes)
    recipesRecuperadas= json.loads(response)
    respuesta = jsonify({
            "message": "Recipes", 
            "status": 200,
            "data": recipesRecuperadas
            }
        )
    return Response(response, mimetype="application/json")

#Se obtiene una receta en especifico
@app.route("/getRecipeu/<id>/",  methods=["GET"])
def get_recipeId(id):
    receta = mongo.db.recipes.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(receta)
    return Response(response, mimetype="application/json")

@app.route("/recipeTotal", methods=["GET"])
def get_recipesTotal():
    headers = {"Content-Type": "application/json"}
    
    recipes = mongo.db.recipes.find()
    response = json_util.dumps(recipes)
    recipesRecuperadas= json.loads(response)
    resultado = dict()
    
    print(type(response))
    for x in recipesRecuperadas:
        #conteo = Counter(x["ingredients"])
        
        ingredientes = x["ingredients"]
        for ing in ingredientes:  
            if(ing in resultado):
                resultado[ing] +=1
            else:
                resultado[ing] = 1
            #valor=conteo[clave]

            #if valor != 1:
                #resultado[clave] = valor

                #if resultado.key(clave) != None:
                    #resultado[clave] = resultado[clave] + valor
                #else:   
                    #resultado[clave] = valor         
        #print(re)
    resultadoOr = dict(sorted(resultado.items(), key=lambda item: item[1]))
    #resultadoOr = collections.OrderedDict(resultado)
    print(resultadoOr)
    
    respuesta = jsonify({
            "message": "Recipes", 
            "status": 200,
            "data": recipesRecuperadas
            }
        )
    return Response(response, mimetype="application/json")


#Este metodo añade una receta, perteneciente a un usuario
@app.route("/recipe/add", methods=["POST"])
def create_recipe():
    nombre = request.json["nombre"]
    img = request.json["img"]
    tiempo = request.json["tiempo"]
    ingredientes = request.json["ingredientes"]
    instrucciones = request.json["instrucciones"]
    pais = request.json["pais"]
    diet = request.json["diet"]
    author = request.json["author"]

    recip = mongo.db.recipes.insert_one(
        {
            "nombre": nombre,
            "img": img,
            "tiempo": tiempo,
            "ingredientes": ingredientes,
            "instrucciones": instrucciones,
            "pais": pais,
            "diet": diet,
            "author": author,
        }
    )
    return "hallo"

#Este metodo añade una receta a los favoritos del usuario
@app.route("/addfavorite/<email>/", methods=["PUT"])
def add_recipe_favorite(email):
    favorites = request.json["favorites"]
    mongo.db.users.update_one({"usuario": email}, {"$set": {"favorites": favorites}})
    return Response({"status": 200, "mensaje": "actualizacion exitosa"}, mimetype="application/json")

#Retorna las recetas de un autor
@app.route("/<email>/recipes", methods=["GET"])
def get_user_recipes(email):
    recipes = mongo.db.recipes.find({"author": email})
    response = json_util.dumps(recipes)
    return Response(response, mimetype="application/json")


#Añade un usuario a la base de datos
@app.route("/user/add", methods=["POST"])
def create_user():
    usuario = request.json["usuario"]
    password = request.json["password"]
    recipes = request.json["recipes"]
    favorites = request.json["favorites"]
    mensaje = request.json["mensaje"]
    pais = request.json["pais"]

    user = mongo.db.users.find_one({"usuario": usuario})

    if user is None:
        hashed_password = generate_password_hash(password)
        id = mongo.db.users.insert_one(
            {
                "usuario": usuario,
                "password": hashed_password,
                "recipes": recipes,
                "favorites": favorites,
                "pais": pais,
                "mensaje": mensaje,
            }
        )

        headers = {"Content-Type": "application/json"}
        respuesta = jsonify({
            "mensaje": "Usuario creado con exito",
            "status": 200
        })
        #return Response(response, mimetype="application/json")
        return make_response(respuesta, 200, headers)
    else:
        headers = {"Content-Type": "application/json"}
        respuesta = jsonify(
            {"message": "El usuario ya existe", "status": 404}
        )
        return make_response(respuesta, 200, headers)

#Valida si un usuario esta en la base de datos
@app.route("/user/validate", methods=["POST"])
def validate_user():
    headers = {"Content-Type": "application/json"}
    usuario = request.json["usuario"]
    password = request.json["password"]

    user = mongo.db.users.find_one({"usuario": usuario})

    jsuser = json_util.dumps(user)
    usuarioRecuperado = json.loads(jsuser)
    print(usuarioRecuperado)
    if usuarioRecuperado["usuario"] == usuario :
        respuesta = jsonify({
            "message": "El usuario existe", 
            "status": 200,
            "data": usuarioRecuperado
            }
        )
        return make_response(respuesta, 200, headers)
    else:
        response = jsonify({"message": "Usuario no existe ", "status": 404})
        return response

#Retorna todos los usuarios
@app.route("/users", methods=["GET"])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype="application/json")

#Busca un usuario en especifico por id
@app.route("/user/<id>", methods=["GET"])
def get_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    print(id)
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")

#Busca un usaurio por el nombre de usuaior
@app.route("/usere/<email>", methods=["GET"])
def get_usere(email):
    user = mongo.db.users.find_one({"email": email})
    print(id)
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")

#Error
@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({"message": "Resource Not foud" + request.url, "status": 404})
    response.status_code(404)
    return response
