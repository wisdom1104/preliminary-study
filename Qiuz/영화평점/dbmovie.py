target_movie = db.movies.find_one({'title':'가버나움'})
target_star = target_movie['star']

movies = list(db.movies.find({'star':target_star}))

for movie in movies:
    print(movie['title'])