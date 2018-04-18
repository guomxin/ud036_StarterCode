#-*- encoding: utf-8 -*-

class Movie():
    """本类存储电影相关的信息，存储的信息包括：电影名、海报URL、预告片Youtube URL
    Attributes:
        title (str): 电影名称
        poster_image_url (str): 海报图片URL
        trailer_youtube_url (str): 预告片Youtube播放地址
    """
    
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
