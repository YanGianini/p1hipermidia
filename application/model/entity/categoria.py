
class Categoria():
    def __init__(self, id, titulo, descricao, url_img):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.url_img = url_img
        self.videos = []

    def get_id(self):
        return self.id

    def get_id(self, id):
        self.id = id

    def get_videos(self):
        return self.videos

    def add_video(self, video):
        self.videos.append(video)

    def get_titulo(self):
        return self.titulo

    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_descricao(self):
        return self.descricao

    def set_descricao(self, descricao):
        self.descricao = descricao

    def get_url_img(self):
        return self.url_img

    def set_url_img(self, url_img):
        self.url_img = url_img

