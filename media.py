"""Import The Browser"""
import webbrowser

"""Using Class Movie"""


class Movie():
    def __init__(self,
                 movie_title,
                 release_date,
                 earnings,
                 poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.release_date = release_date
        self.earnings = earnings
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
