from flask import Flask
import os
from application.model.entity.video import Video
from application.model.entity.categoria import Categoria


app = Flask(__name__, static_folder=os.path.abspath("application/view/static"), template_folder=os.path.abspath("application/view/templates"))


video1 = Video(1, "https://www.youtube.com/embed/adLGHcj_fmA", "urls da img", "titulo aqui1", 'descrição aqui', 4, "10/03/2021", "humor")
video2 = Video(2, "https://www.youtube.com/embed/uNT_AxXrUGs", "urls da img", "titulo aqui2", 'descrição aqui', 1, "23/05/2021", "humor")
video3 = Video(3, "urls", "urls da img", "titulo aqui3", "descrição aqui", 2, "02/12/2021", "humor")

video4 = Video(4, "urls", "urls da img", "titulo aqui4", "descrição aqui", 3, "02/12/2021", "musica")
video5 = Video(5, "urls", "urls da img", "titulo aqui5", "descrição aqui", 5, "02/12/2021", "musica")
video6 = Video(6, "urls", "urls da img", "titulo aqui6", "descrição aqui", 1, "02/12/2021", "musica")

video7 = Video(7, "urls", "urls da img", "titulo aqui7", "descrição aqui", 1, "02/12/2021", "comida")
video8 = Video(8, "urls", "urls da img", "titulo aqui8", "descrição aqui", 9, "02/12/2021", "comida")
video9 = Video(9, "urls", "urls da img", "titulo aqui9", "descrição aqui", 7, "02/12/2021", "comida")

videos = [video1, video2, video3, video4, video5, video6, video7, video8, video9]

categoria1 = Categoria(1, "humor", "coisas engraçadas no geral", "urls aqui")
categoria2 = Categoria(2, "musica", "musicas de diversos generos", "urls")
categoria3 = Categoria(3, "comida", "receitas e culinaria", "urls")

categorias = [categoria1, categoria2, categoria3]

categoria1.add_video(video1)
categoria1.add_video(video2)
categoria1.add_video(video3)

categoria2.add_video(video4)
categoria2.add_video(video5)
categoria2.add_video(video6)

categoria3.add_video(video7)
categoria3.add_video(video8)
categoria3.add_video(video9)


from application.controller import home_controller