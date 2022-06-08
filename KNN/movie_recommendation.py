""" the KNN (k nearest neighbors) algorithm is usually used for classification
or regression (prediction). but here, I used it for a movie recommendation system.
when a user watches a movie, the system recommands that movie for K users who have
the nearest movie tastes as the user who watched the movie."""
users = dict()
# the tuple value for each key is a collection of the user's average ratings
# for movies of genre: action, comedy, romance, scify, drama ( from 1 to 5)
users["sami"] = (4, 3, 2, 5, 1)
users["yabsra"] = (5, 3, 2, 4, 4)
users["hanye"] = (1, 4, 2, 1, 4)
users["dagi"] = (5,1,5,5,4,)
users["etetu"] = (0,5,3,5,0,)
users["aba"] = (0,3,0,5,0,)
users["micky"] = (3,0,0,5,3,)
users["zersh"] = (0,0,0,2,4,)
users["driba"] = (1,3,3,0,4,)
users["ashenafi"] = (4,2,5,4,2,)
users["addis"] = (4,5,1,5,3,)


def recommend(user, movie, k):
    """gets a user and the movie a user just watched. then recommends the movie to
    the k nearest neighbors of user."""

    # calculate the distace of each neighbor from user:
    nearest_neighbors = []
    for neighbor, neighbor_rating in users.items():
        if neighbor == user:
            continue
        distance = 0
        for i in range(len(neighbor_rating)):
            distance += (users[user][i] - neighbor_rating[i])**2
        nearest_neighbors.append((neighbor, distance))

    # sort with the distances
    nearest_neighbors.sort(key=lambda x: x[1])
    
    # print a message that the movie has been recommended.
    for i in range(k):
        print(movie, "is recommended to", nearest_neighbors[i][0])

recommend('zersh', "The dark night", 4)