# Tim Coyle
# 9/3/15
# Version 1.0

# Description
# Create a movie trailer website in Python (based on Udacity course Python Foundations)

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=vwyZH85NQC4")
# debug line
#print(toy_story.storyline)

avatar = media.Movie("Avatar",
                        "A marine on an alien planet",
                        "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg",
                        "https://www.youtube.com/watch?v=aVdO-cx-McA")
# debug line
#avatar.show_trailer()

# setup array of movies to pass to function that will create movie trailer website
movies = [toy_story,avatar]

# this python file will create an html file with movie trailers than can be played
fresh_tomatoes.open_movies_page(movies)