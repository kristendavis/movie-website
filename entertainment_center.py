'''This is a file used to store movie data formatted according to the Movie
class and run the fresh_tomatoes program to launch the webpage'''
import media
import fresh_tomatoes

'''The library of movies including each movie's title, lead actors, summary,
rating, poster and trailer'''
his_girl_friday = media.Movie("His Girl Friday",
                              "Cary Grant, Rosalind Russell",
                              '''A newspaper editor uses every trick in the
                              book to keep his ace reporter
                              ex-wife from remarrying.''',
                              media.Movie.VALID_RATINGS[4],
                              "https://aworldoffilm.files.wordpress.com/2014/01/azbzeds2uymgbsndqutvaeu2dha.jpg",
                              "https://www.youtube.com/watch?v=dHVvnEWez1M")

xfiles_fight_the_future = media.Movie("The X-Files: Fight the Future",
                                      "Gillian Anderson, David Duchovny",
                                      '''Mulder and Scully must fight the
                                      government in a conspiracy and find the
                                      truth about an alien colonization of
                                      Earth.''',
                                      media.Movie.VALID_RATINGS[2],
                                      "https://upload.wikimedia.org/wikipedia/en/thumb/6/6c/XFilesMoviePoster.jpg/220px-XFilesMoviePoster.jpg",
                                      "https://www.youtube.com/watch?v=kk0inzcZmaE")

charade = media.Movie("Charade",
                      "Cary Grant, Audrey Hepburn",
                      '''Romance and suspense ensue in Paris as a woman is
                      pursued by several men who want a fortune her murdered
                      husband had stolen. Who can she trust?''',
                      media.Movie.VALID_RATINGS[4],
                      "https://s-media-cache-ak0.pinimg.com/736x/32/ba/6d/32ba6d69dd4855602e1cebcabf58e7bf.jpg",
                      "https://www.youtube.com/watch?v=QmgPw34Xm3A")

howls_moving_castle = media.Movie("Howl's Moving Castle",
                                  "Christian Bale, Emily Mortimer",
                                  '''When an young woman is cursed by a
                                  spiteful witch, her only chance of breaking
                                  the spell lies with a self-indulgent young
                                  wizard and his walking castle.''',
                                  media.Movie.VALID_RATINGS[1],
                                  "http://www.nausicaa.net/miyazaki/howl/poster_images/USA_full.jpg",
                                  "https://www.youtube.com/watch?v=iwROgK94zcM")

serenity = media.Movie("Serenity",
                       "Nathan Fillion, Gina Torres",
                       '''The crew of the ship Serenity tries to evade an
                       assassin sent to recapture one of their number who is
                       telepathic.''',
                       media.Movie.VALID_RATINGS[2],
                       "http://www.gstatic.com/tv/thumb/movieposters/89596/p89596_p_v8_ac.jpg",
                       "https://www.youtube.com/watch?v=JY3u7bB7dZk")

cats_dont_dance = media.Movie("Cats Don't Dance",
                              "Scott Bakula, Jasmine Guy",
                              '''Danny, an ambitious singing/dancing cat, goes
                              to Hollywood and overcomes several obstacles to
                              fulfill his dream of becoming a movie star.''',
                              media.Movie.VALID_RATINGS[0],
                              "http://www.gstatic.com/tv/thumb/movieposters/19184/p19184_p_v8_aa.jpg",
                              "https://www.youtube.com/watch?v=EAet5fsSYbc")

# A list used to store the movies and their data
movies = [his_girl_friday, xfiles_fight_the_future, charade,
          howls_moving_castle, serenity, cats_dont_dance]

# Launches webpage with input movies
fresh_tomatoes.open_movies_page(movies)
