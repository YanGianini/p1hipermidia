from application import videos
from application.model.entity.video import Video

class VideoDAO():
    def __init__(self):
        self.videos = videos

    def lista_videos(self):
        return self.videos

