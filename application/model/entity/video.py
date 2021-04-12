
class Video():
    def __init__(self, id, url_video, url_img, titulo, descricao, qtd_curtidas, data, categoria):
        self.id = id
        self.url_video = url_video
        self.url_img = url_img
        self.titulo = titulo
        self. descricao = descricao
        self.qtd_curtidas = qtd_curtidas
        self.data = data
        self.categoria = categoria

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_url_video(self):
        return self.url_video

    def set_url_video(self, url):
        self.url_video = url

    def get_url_img(self):
        return self.url_img

    def set_url_img(self, url):
        self.url_img = url

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_qtd_curtidas(self):
        return self.qtd_curtidas

    def set_qtd_curtidas(self, qtd):
        self.qtd_curtidas = qtd 

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_categoria(self):
        return self.categoria

    def set_categoria(self, categoria):
        self.categoria = categoria
