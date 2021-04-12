from application import app
from flask import render_template, redirect, request, url_for
from application.model.dao.categoriaDAO import CategoriaDAO

@app.route("/")
def index():
    categoriaDAO = CategoriaDAO()
    listaCategorias = categoriaDAO.lista_categorias()
    return render_template("index.html", listaCategorias = listaCategorias)


@app.route("/videos")
def videos():
    return render_template("videos.html")
