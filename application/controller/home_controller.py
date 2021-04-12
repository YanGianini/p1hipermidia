from application import app
from flask import render_template, redirect, request, url_for
from application.model.dao.categoriaDAO import CategoriaDAO
from application.model.dao.videoDAO import VideoDAO

@app.route("/")
def index():
    categoriaDAO = CategoriaDAO()
    listaCategorias = categoriaDAO.lista_categorias()
    return render_template("index.html", listaCategorias = listaCategorias)


@app.route("/videos/<id>")
def videos(id):
    videos = VideoDAO()
    for video in videos.lista_videos():
        if str(video.get_id())== id:
            return render_template("videos.html", video=video)
        


