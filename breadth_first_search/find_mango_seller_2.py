"""the same algorithm but the book's way"""

# THIS IS A DIRECTED GRAPH
from collections import deque
from codetimer import Timer


graph = dict()
graph["you"] = ["bob", "claire", "alice"]
graph["alice"] = ["peggy",]
graph["bob"] = ["peggy", "anuj"]
graph["claire"] = ["thon", "jonny"]
graph["peggy"] = []
graph["anuj"] = []
graph["jonny"] = []
graph["thon"] = []


def person_is_seller(name):
    """let's say mango sellers have names ending with 'n'"""
    return name[-1] == 'y'


def BFS(you):
    """does a breadth-forst-search to find the closest mango seller. 'you' is the entry 
    point of the search"""
    searchQueue = deque()
    searchQueue.append(you)

    while len(searchQueue) > 0:
        person = searchQueue.popleft()
        if person_is_seller(person):
            return person
        else:
            searchQueue += graph[person]
    return None


# change the input to 'claire' and the BFS should return 'jhonny'. because jhonny
# closer to bob than peggy is. On the other hand, giving 'anuj' to the BFS returns
# None because we have a directed graph.

with Timer():
    print(BFS("bob"))
