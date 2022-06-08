"""the KNN (k nearest neighbors) algorithm is usually used for classification
and regression (prediction). In this code, I used KNN to predict how a movie will be
rated by a user by looking at how it's rated by the K people who have the nearest
tastes for movies as the user whose rating we're trying to predict. This code simply
uses the distance formula to identify users with similar preferences. It can be improved
by implementing cosine similarity instead of the distance formula."""

from random import random

class User:
    def __init__(self, name, genre_ratings):
        self.name = name
        self.genre_ratings = genre_ratings;
        self.movie_ratings = {}
    def __repr__(self):
        return f"{self.name} : home {self.movie_ratings['home']}"



# a dictionary containing all the user entities
users = {
    "sami": User("sami", {"action":4, "comedy":3, "romance":2, "scify":5, "drama":1}),
    "yabsra": User("yabsra", {"action":5, "comedy":3, "romance":2, "scify":4, "drama":4}),
    "hanye": User("hanye", {"action":1, "comedy":4, "romance":2, "scify":1, "drama":4}),
    "dagi": User("dagi", {"action":5, "comedy":1, "romance":5, "scify":5, "drama":4}),
    "etetu": User("etetu", {"action":0, "comedy":5, "romance":3, "scify":5, "drama":0}),
    "aba": User("aba", {"action":0, "comedy":3, "romance":0, "scify":5, "drama":0}),
    "micky": User("micky", {"action":3, "comedy":0, "romance":0, "scify":5, "drama":3}),
    "zersh": User("zersh", {"action":0, "comedy":0, "romance":0, "scify":2, "drama":4}),
    "drriba": User("drriba", {"action":1, "comedy":3, "romance":3, "scify":0, "drama":4}),
    "ashenafi": User("ashenafi", {"action":4, "comedy":2, "romance":5, "scify":4, "drama":2}),
    "addis": User("addis", {"action":4, "comedy":5, "romance":1, "scify":5, "drama":3})
}

new_user = User("hesita", {"action":2, "comedy":3, "romance":5, "scify":2, "drama":5})

for name in users.keys():
    users[name].movie_ratings["home"] = int(random()*6)

def predict_rating(user, movie):
    # first find the 5 nearest neighbors
    # the 'data list holds tuples containing the names of neighbors and their respective distances
    data = []
    for name in users:
        distance = 0
        for key in users[name].genre_ratings.keys():
            distance += (new_user.genre_ratings[key] - users[name].genre_ratings[key])**2
        data.append([name, distance])
    data.sort(key=lambda x: x[1])
    data = data[:5]

    # we need to manipulate the distances to generate weights we can use to do the weighted mean
    max_distance = data[-1][1]
    min_distance = data[0][1]
    transform_factor = (max_distance - min_distance) * 0.1
    for item in data:
        item[1] = max_distance - item[1] + transform_factor + 1

    # now do the weighted mean
    total_sum = 0
    weight_sum = 0
    for item in data:
        total_sum += users[item[0]].movie_ratings[movie] * item[1]
        weight_sum += item[1]

    for i in range(5):
        print(data[i][0], data[i][1], "rated", movie, users[data[i][0]].movie_ratings[movie])

    return total_sum/weight_sum


print("The prediction is that", new_user.name, "will rate 'Home'", predict_rating(new_user, "home"), "points")
