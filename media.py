import webbrowser


__author__ = "Kristen Davis"
__credits__ = "Udacity Team"


class Movie():
    '''The Movie class is used to assign a movie the information included
	in the __init__ function and show a trailer of each movie object.
	'''
    VALID_RATINGS = ["G", "PG", "PG-13", "R", "NR"]

    def __init__(self, movie_title, lead_actors, movie_storyline,
                 movie_rating, poster_image, trailer_youtube):
        '''Assigns variable names to function inputs for use in the webpage
        '''
        self.title = movie_title
        self.actors = lead_actors
        self.storyline = movie_storyline
        self.rating = movie_rating
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        '''Takes the movie as input, opens a url to show a movie trailer
        '''
        webbrowser.open(self.trailer_youtube_url)
