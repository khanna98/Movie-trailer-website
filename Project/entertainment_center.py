import fresh_tomatoes
import media


toy_story = media.Movie("Toy Story","A story of a boy and his toys that come to life.","https://lumiere-a.akamaihd.net/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0%2C0%2C300%2C450","https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar","A marine on alien planet","https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg","https://www.youtube.com/watch?v=5PSNL1qE6VY")

school_of_rock = media.Movie("School Of Rock","Using rock music to learn","https://images-na.ssl-images-amazon.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_UX182_CR0,0,182,268_AL_.jpg","https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille","A rat is a chef in Paris","https://vignette2.wikia.nocookie.net/disney/images/7/71/Ratatouille1.jpg/revision/latest?cb=20150926074207&path-prefix=it","https://www.youtube.com/watch?v=iCMGPRiDXQg")

midnight_in_paris = media.Movie("Midnight in Paris","Going Back in time to meet authors.","https://images-na.ssl-images-amazon.com/images/I/61-nVJ7VKxL.jpg","https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger Games","A really real reality show","https://images-na.ssl-images-amazon.com/images/I/91ikvZgoHZL._SL1500_.jpg","https://www.youtube.com/watch?v=mfmrPu43DF8")


movies = [toy_story,avatar,school_of_rock,ratatouille,midnight_in_paris,hunger_games]
fresh_tomatoes.open_movies_page(movies)