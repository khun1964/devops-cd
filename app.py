# from flask import Flask 
# import os

# # Récupération des ENVs

# PORT = os.environ.get("PORT", "80")
# HOST = os.environ.get("HOST", "0.0.0.0")

# app = Flask("demo")

# @app.get("/")
# def hello():
    
#      """ Fonction appelé pour le chemin par défaut.
     
#      Returns :
#         str: un message de la plus grande importance.
#      """   
    
#     return "hello world !"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=80)
    
    
    """_summary_
    projet de demo pour la création d'un CD

    Returns:
        _type_: _description_
    """

from flask import Flask
import os

# Recuperation des ENVs
PORT = os.environ.get("PORT", "80")
HOST = os.environ.get("HOST", "0.0.0.0")

app = Flask("demo")

@app.get("/")
def hello():
    
    """
    Fonction appelee pour le chemin par defaut.
    Returns:
        str: un message :
    """
    return "hello world!"


if __name__ == "__main__":
    app.run(host="HOST", port=PORT)


    