"""Import Fresh Tomatoes & media"""
import fresh_tomatoes

import media

book_of_life = media.Movie("The Book of Life",
                           "October 17, 2014",
                           "$953 Million",
                           "http://s27.postimg.org/owonlapyr/tbol.jpg",
                           "https://www.youtube.com/watch?v=NBw5YScs8iQ")

night_at_the_museum = media.Movie("Night at the Museum",
                                  "December 19, 2014",
                                  "$360.2 Million",
                                  "http://s27.postimg.org/5svc4yd4j/natm.jpg",
                                  "https://www.youtube.com/watch?v=KMKk7Dn__-Y"
                                  )

the_imitation_game = media.Movie("The Imitation Game",
                                 "March 31, 2015",
                                 "$1215.5 Million",
                                 "http://s27.postimg.org/lfmlibqwj/tig.jpg",
                                 "https://www.youtube.com/watch?v=S5CjKEFb-sM")

tinker_bell = media.Movie("Tinker Bell",
                          "December 12, 2014",
                          "$167 Million",
                          "http://s27.postimg.org/hxallxq0j/tib.jpg",
                          "https://www.youtube.com/watch?v=ofvJ7KyulPA")

avengers = media.Movie("Avengers: Age of Ultron",
                       "May 1, 2015",
                       "$881.2 Million",
                       "http://s27.postimg.org/5wp5l7ilv/ataou.jpg",
                       "https://www.youtube.com/watch?v=iSAyI1HBD6s")

monsters_university = media.Movie("Monsters University",
                                  "June 21, 2013",
                                  "$743.6 Million",
                                  "http://s27.postimg.org/nb9dthfqr/image.jpg",
                                  "https://www.youtube.com/watch?v=xBzPioph8CI"
                                  )

"""Calling the media objects in Fresh tomatoes file"""
movies = [book_of_life,
          night_at_the_museum,
          the_imitation_game,
          tinker_bell,
          avengers,
          monsters_university]
fresh_tomatoes.open_movies_page(movies)
