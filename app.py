from flask import Flask, jsonify, request, Response, make_response, flash, redirect

from PIL import Image 
from collections import Counter
from werkzeug.utils import secure_filename

import collections
import json
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
from bson import json_util
from bson.objectid import ObjectId


app = Flask(__name__)


app.config[
    "MONGO_URI"
] = "mongodb+srv://OtterFox:sqbZeoBKy8Qp6fd@cluster0.uwltrza.mongodb.net/mineria"

mongo = PyMongo(app)

# Este metodo recupera todas las recetas disponibles
@app.route("/recipetwy", methods=["GET"])
def get_recipestwy():
    headers = {"Content-Type": "application/json"}
    recipes = mongo.db.recipes.find()
    response = json_util.dumps(recipes)
    recipesRecuperadas = json.loads(response)
    respuesta = jsonify(
        {"message": "Recipes", "status": 200, "data": recipesRecuperadas}
    )
    return Response(response, mimetype="application/json")


@app.route("/recipes/<size>/<pag>", methods=["GET"])
def get_recipe_pag(size, pag):
    skips = int(size) * (int(pag) - 1)
    recipe = mongo.db.recipes.find().skip(skips).limit(int(size))
    response = json_util.dumps(recipe)
    return Response(response, mimetype="application/json")


@app.route("/recipes/ingredientes", methods=["POST"])
def get_recipe_ingredientes():
    ingredintes = request.json["ingredientes"]
    recipes = mongo.db.recipes.find()
    response = json_util.dumps(recipes)
    iteracion = json.loads(response)
    respuesta = []
    for x in iteracion:
        esta = True
        for y in ingredintes:
            if y in x["ingredients"]:
                esta = True
            else:
                esta = False
                break
        if esta:
            respuesta.append(x)
    # print(respuesta)
    diccionario = {"data": respuesta}
    return diccionario

@app.route("/opencv", methods=["POST"])
def opencv():
    # print("Posted file: {}".format(request.files['data']))
    file = request.files["file"]
    
    
    #image = np.asarray(bytearray(file.read()), dtype="uint8")

    #numpy.fromstring(request.files["file"].read(), numpy.uint8)
    #imagen1 = cv2.imdecode(image, cv2.IMREAD_COLOR)
    #imagen2 = cv2.imdecode(image, cv2.IMREAD_COLOR)


    new_width = 200
    new_height = 200

    dsize = (new_width, new_height)
 
# redimencionar la image
    #output = cv2.resize(imagendecode, dsize, interpolation = cv2.INTER_AREA)
    #imagenes.append(output)
    

    #concat_vertical = cv2.vconcat([imagen1, imagen2])

    #im = Image.open(concat_vertical)

   # im.save('./cover_2.jpg', format='JPEG', quality=95)

   #cv2.imshow('concat_vertical', concat_vertical)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    diccionario = {
        "status": 200,
        "ingredientsDetected": ["apple", "cheese"],
        "data": [
            {
                "_id": {"$oid": "62f3cf79944789e684ef1213"},
                "countedElements": 1,
                "duration": "1 hora",
                "imageUrl": "https://www.cocina-ecuatoriana.com/base/stock/Recipe/310-image/310-image_web.jpg",
                "ingredients": [
                    "squid",
                    "Garlic",
                    "cumin",
                    "Salt",
                    "lemon",
                    "egg",
                    "flour",
                    "bread",
                    "oil",
                    "Pepper",
                ],
                "link": "https://www.cocina-ecuatoriana.com/recetas/entradas/calamares-fritos",
                "steps": [
                    "Lavar bien los calamares y córtelos en ruedas.",
                    "Coloque los calamares en un bol y agregue el ajo machacado, comino, pimienta, salsa de soya y el jugo de limón.",
                    "Mezcle bien todos los ingredientes y cubra el bol con papel film. Deje macerar en el refrigerador por unas 2 horas aproximadamente.",
                    "Transcurrido el tiempo de maceración, pase los calamares por harina, luego por huevo batido y por último por la miga de pan.",
                    "Fría los calamares en aceite bien caliente hasta que se doren.",
                    "Sírvalos decorados con rodajas de limón y acompañados con alguna salsa de su preferencia.",
                ],
                "title": "Calamares fritos",
            },
            {
                "_id": {"$oid": "62f3cf79944789e684ef1213"},
                "countedElements": 1,
                "duration": "1 hora",
                "imageUrl": "https://www.cocina-ecuatoriana.com/base/stock/Recipe/310-image/310-image_web.jpg",
                "ingredients": [
                    "squid",
                    "Garlic",
                    "cumin",
                    "Salt",
                    "lemon",
                    "egg",
                    "flour",
                    "bread",
                    "oil",
                    "Pepper",
                ],
                "link": "https://www.cocina-ecuatoriana.com/recetas/entradas/calamares-fritos",
                "steps": [
                    "Lavar bien los calamares y córtelos en ruedas.",
                    "Coloque los calamares en un bol y agregue el ajo machacado, comino, pimienta, salsa de soya y el jugo de limón.",
                    "Mezcle bien todos los ingredientes y cubra el bol con papel film. Deje macerar en el refrigerador por unas 2 horas aproximadamente.",
                    "Transcurrido el tiempo de maceración, pase los calamares por harina, luego por huevo batido y por último por la miga de pan.",
                    "Fría los calamares en aceite bien caliente hasta que se doren.",
                    "Sírvalos decorados con rodajas de limón y acompañados con alguna salsa de su preferencia.",
                ],
                "title": "Calamares fritos",
            }
        ],
    }
    return diccionario
    
    # image = {'image': file.read()}
    # print(image)
    # headers = {
    # "Content-Type": "multipart/form-data",
    # }
    # ficheros = {
    #   "image": image
    # }
    return "oka"
    # r = requests.post("https://api.imgbb.com/1/upload?expiration=600&key=5eb17d3638835e60af978041f015e33c",headers=headers, files=image)
    # print(r)
    # if r.ok:

# Guarda una imagen
@app.route("/savePhto", methods=["POST"])
def post_photo():
    # print("Posted file: {}".format(request.files['data']))
    files = request.files["file0"]
    print(files)
    print(type(files))
    imagenes = []
    #print(file)
    for file in request.files:
       fil = request.files[file]
       #image = np.asarray(bytearray(fil.read()), dtype="uint8")
      # imagendecode = cv2.imdecode(image, cv2.IMREAD_COLOR)
       new_width = 200
       new_height = 200
# dsize
       dsize = (new_width, new_height)
 
# redimencionar la image
      # output = cv2.resize(imagendecode, dsize, interpolation = cv2.INTER_AREA)
       #imagenes.append(output)
      
    #imagen1 = cv2.imread("imagen2.jpg")
    #imagen2 = cv2.imread("imagen2.jpg")
    
    #image = np.asarray(bytearray(file.read()), dtype="uint8")
    #numpy.fromstring(request.files["file"].read(), numpy.uint8)
    #imagen1 = cv2.imdecode(image, cv2.IMREAD_COLOR)
    #imagen2 = cv2.imdecode(image, cv2.IMREAD_COLOR)
    
   # concat_vertical = cv2.vconcat(imagenes)
    #cv2.imwrite('./imagencombinada.png',concat_vertical) 
    #cv2.imshow('concat_vertical', concat_vertical)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()
    
    diccionario = {
        "status": 200,
        "ingredientsDetected": ["appel", "cumin", "oil"],
        "data": [
            {
                "_id": {"$oid": "62f3cf79944789e684ef1213"},
                "countedElements": 1,
                "duration": "1 hora",
                "imageUrl": "https://www.cocina-ecuatoriana.com/base/stock/Recipe/310-image/310-image_web.jpg",
                "ingredients": [
                    "squid",
                    "Garlic",
                    "cumin",
                    "Salt",
                    "lemon",
                    "egg",
                    "flour",
                    "bread",
                    "oil",
                    "Pepper",
                ],
                "link": "https://www.cocina-ecuatoriana.com/recetas/entradas/calamares-fritos",
                "steps": [
                    "Lavar bien los calamares y córtelos en ruedas.",
                    "Coloque los calamares en un bol y agregue el ajo machacado, comino, pimienta, salsa de soya y el jugo de limón.",
                    "Mezcle bien todos los ingredientes y cubra el bol con papel film. Deje macerar en el refrigerador por unas 2 horas aproximadamente.",
                    "Transcurrido el tiempo de maceración, pase los calamares por harina, luego por huevo batido y por último por la miga de pan.",
                    "Fría los calamares en aceite bien caliente hasta que se doren.",
                    "Sírvalos decorados con rodajas de limón y acompañados con alguna salsa de su preferencia.",
                ],
                "title": "Calamares fritos",
            },
            {
                "_id": {"$oid": "62f3cf79944789e684ef1213"},
                "countedElements": 1,
                "duration": "1 hora",
                "imageUrl": "https://www.cocina-ecuatoriana.com/base/stock/Recipe/310-image/310-image_web.jpg",
                "ingredients": [
                    "squid",
                    "Garlic",
                    "cumin",
                    "Salt",
                    "lemon",
                    "egg",
                    "flour",
                    "bread",
                    "oil",
                    "Pepper",
                ],
                "link": "https://www.cocina-ecuatoriana.com/recetas/entradas/calamares-fritos",
                "steps": [
                    "Lavar bien los calamares y córtelos en ruedas.",
                    "Coloque los calamares en un bol y agregue el ajo machacado, comino, pimienta, salsa de soya y el jugo de limón.",
                    "Mezcle bien todos los ingredientes y cubra el bol con papel film. Deje macerar en el refrigerador por unas 2 horas aproximadamente.",
                    "Transcurrido el tiempo de maceración, pase los calamares por harina, luego por huevo batido y por último por la miga de pan.",
                    "Fría los calamares en aceite bien caliente hasta que se doren.",
                    "Sírvalos decorados con rodajas de limón y acompañados con alguna salsa de su preferencia.",
                ],
                "title": "Calamares fritos",
            }
        ],
    }
    return diccionario
    
    # image = {'image': file.read()}
    # print(image)
    # headers = {
    # "Content-Type": "multipart/form-data",
    # }
    # ficheros = {
    #   "image": image
    # }
    return "oka"
    # r = requests.post("https://api.imgbb.com/1/upload?expiration=600&key=5eb17d3638835e60af978041f015e33c",headers=headers, files=image)
    # print(r)
    # if r.ok:


# Recetas mas recientes
@app.route("/recipes/recient", methods=["GET"])
def get_recipe_recients():
    recipes = mongo.db.recipes.find().sort("_id", -1).limit(10)
    response = json_util.dumps(recipes)
    return Response(response, mimetype="application/json")


# Recetas Ecuador


# Se obtiene una receta en especifico
@app.route("/getRecipeu/<id>/", methods=["GET"])
def get_recipeId(id):
    receta = mongo.db.recipes.find_one({"_id": ObjectId(id)})
    response = json_util.dumps(receta)
    return Response(response, mimetype="application/json")


# Se obtiene una receta en especifico
@app.route("/getRecipesF", methods=["POST"])
def get_recipeFav():
    headers = {"Content-Type": "application/json"}
    recetas_recuperadas = []
    recetas = request.json["recetas"]
  
    if len(recetas) > 0:
        print("entro")
        for x in recetas:
            receta = mongo.db.recipes.find_one({"_id": ObjectId(x)})
            objeto = json_util.dumps(receta, indent=2)
            recetas_recuperadas.append(json.loads(objeto))
   
    # receta = mongo.db.recipes.find_one({"_id": ObjectId(id)})
    #res = jsonify(items=[dict(a=1, b=2), dict(c=3, d=4)])
    #response = json_util.dumps(recetas_recuperadas)
    #print(recetas_recuperadas[0])
    #respuesta = jsonify(
       # {"message": "Recipes", "status": 200, "data": recetas_recuperadas}
    #)
    diccionario = {"data": recetas_recuperadas}
    return diccionario


@app.route("/recipeTotal", methods=["GET"])
def get_recipesTotal():
    headers = {"Content-Type": "application/json"}

    recipes = mongo.db.recipes.find()
    response = json_util.dumps(recipes)
    recipesRecuperadas = json.loads(response)
    resultado = dict()

    print(type(response))
    for x in recipesRecuperadas:
        # conteo = Counter(x["ingredients"])

        ingredientes = x["ingredients"]
        for ing in ingredientes:
            if ing in resultado:
                resultado[ing] += 1
            else:
                resultado[ing] = 1
            # valor=conteo[clave]

            # if valor != 1:
            # resultado[clave] = valor

            # if resultado.key(clave) != None:
            # resultado[clave] = resultado[clave] + valor
            # else:
            # resultado[clave] = valor
        # print(re)
    resultadoOr = dict(sorted(resultado.items(), key=lambda item: item[1]))
    # resultadoOr = collections.OrderedDict(resultado)
    print(resultadoOr)

    respuesta = jsonify(
        {"message": "Recipes", "status": 200, "data": recipesRecuperadas}
    )
    return Response(recipesRecuperadas, mimetype="application/json")


# Este metodo añade una receta, perteneciente a un usuario
@app.route("/recipe/add", methods=["POST"])
def create_recipe():
    title = request.json["title"]
    imageUrl = request.json["imageUrl"]
    duration = request.json["duration"]
    ingredients = request.json["ingredients"]
    steps = request.json["steps"]
    pais = request.json["pais"]
    author = request.json["author"]

    id = mongo.db.recipes.insert_one(
        {
            "title": title,
            "imageUrl": imageUrl,
            "duration": duration,
            "ingredients": ingredients,
            "steps": steps,
            "pais": pais,
            "author": author,
        }
    )

    user = mongo.db.users.find_one({"usuario": author})
    jsuser = json_util.dumps(user)
    usuarioRecuperado = json.loads(jsuser)

    recetas = []
    recetas = usuarioRecuperado["recipes"]
    recetas.append(str(id.inserted_id))

    mongo.db.users.update_one({"usuario": author}, {"$set": {"recipes": recetas}})

    print(recetas)

    response = {
        "status": 200,
        "mensaje": "Se añadió correctamente",
        "id": str(id.inserted_id),
    }
    # return Response({"status": 200, "mensaje": "Se añadió correctamente", "id": str(recip)}, mimetype="application/json")
    return response


# Este metodo añade una receta a los favoritos del usuario
@app.route("/addfavorite/<email>/", methods=["PUT"])
def add_recipe_favorite(email):
    favorites = request.json["favorites"]
    mongo.db.users.update_one({"usuario": email}, {"$set": {"favorites": favorites}})
    return Response(
        {"status": 200, "mensaje": "actualizacion exitosa"}, mimetype="application/json"
    )


# Retorna recetas por paises
@app.route("/recipe/country/<pais>", methods=["GET"])
def get_recipes_country(pais):
    country = str(pais)
    recipes = mongo.db.recipes.find({"pais": country})
    response = json_util.dumps(recipes)
    return Response(response, mimetype="application/json")


# Retorna las recetas de un autor
@app.route("/<email>/recipes", methods=["GET"])
def get_user_recipes(email):
    recipes = mongo.db.recipes.find({"author": email})
    response = json_util.dumps(recipes)
    return Response(response, mimetype="application/json")


# Añade un usuario a la base de datos
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
        respuesta = jsonify({"mensaje": "Usuario creado con exito", "status": 200})
        # return Response(response, mimetype="application/json")
        return make_response(respuesta, 200, headers)
    else:
        headers = {"Content-Type": "application/json"}
        respuesta = jsonify({"message": "El usuario ya existe", "status": 404})
        return make_response(respuesta, 200, headers)


# Valida si un usuario esta en la base de datos
@app.route("/user/validate", methods=["POST"])
def validate_user():
    headers = {"Content-Type": "application/json"}
    usuario = request.json["usuario"]
    password = request.json["password"]

    user = mongo.db.users.find_one({"usuario": usuario})

    jsuser = json_util.dumps(user)
    usuarioRecuperado = json.loads(jsuser)

    result = check_password_hash( usuarioRecuperado["password"],password)
    print(result)
    print(usuarioRecuperado)
    if (
        usuarioRecuperado["usuario"] == usuario
        and result
    ):
        respuesta = jsonify(
            {"message": "El usuario existe", "status": 200, "data": usuarioRecuperado}
        )
        return make_response(respuesta, 200, headers)
    else:
        response = jsonify({"message": "Usuario no existe ", "status": 404})
        return response


# Retorna todos los usuarios
@app.route("/users", methods=["GET"])
def get_users():
    users = mongo.db.users.find()
    response = json_util.dumps(users)
    return Response(response, mimetype="application/json")


# Busca un usuario en especifico por id
@app.route("/user/<id>", methods=["GET"])
def get_user(id):
    user = mongo.db.users.find_one({"_id": ObjectId(id)})
    print(id)
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")


# Busca un usaurio por el nombre de usuaior
@app.route("/usere/<email>", methods=["GET"])
def get_usere(email):
    user = mongo.db.users.find_one({"email": email})
    print(id)
    response = json_util.dumps(user)
    return Response(response, mimetype="application/json")


# Error
@app.errorhandler(404)
def not_found(error=None):
    response = jsonify({"message": "Resource Not foud" + request.url, "status": 404})
    response.status_code(404)
    return response
