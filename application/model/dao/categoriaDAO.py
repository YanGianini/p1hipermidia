from application import categorias
from application.model.entity.categoria import Categoria

class CategoriaDAO():
    def __init__(self):
        self.categorias = categorias

    def lista_categorias(self):
        return self.categorias



 