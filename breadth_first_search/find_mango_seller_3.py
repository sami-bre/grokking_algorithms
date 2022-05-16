"""find_mango_seller_2.py has a problem. if we give it undirected graph, it could 
create an infinite loop. to avoid this, we can track who's already searched by maintaining an array"""

from collections import deque

graph = dict()
graph["you"] = ["naomi", "bre"]
graph["bre"] = ["naomi", "you"]
graph["naomi"] = []


def is_seller(name):
    """a name ending with 'q' is a seller :)"""
    return name[-1] == "q"


def BFS_flawed(name):
    """let's do BFS to find the closest seller, but the code has a problem"""
    searchQue = deque()
    searchQue.append(name)
    while searchQue:
        person = searchQue.popleft()
        if is_seller(person):
            return person
        else:
            searchQue += graph[person]
    return None


def BFS_improved(name):
    searchQue = deque()
    searched = []
    searchQue.append(name)

    while searchQue:
        person = searchQue.popleft()
        if person not in searched:
            if is_seller(person):
                return person
            else:
                searchQue += graph[person]
            searched.append(person)
    return None


print(BFS_improved('you'))



