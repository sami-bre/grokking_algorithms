"""The BFS on the book maintains an array of people (nodes) tested so far and checks if the array
contains a node before checking it to avoid checking nodes multiple times. but doing a get operation
on an array takes O(n) by itself. I tired to improve it by attaching a flag to each node telling us
if the node as been in the search queue before so we know which nodes to add to the search queue without
having to do a get for them in an array. but this method sets these flags on on every node after one search
and this should be reversed in order to do another search."""
from collections import deque


class Person:
    def __init__(self, name, *args):
        self.name = name
        self.friends = [item for item in args]
        self.is_seller = False
        self.added_to_q = False

    def __repr__(self):
        return self.name


def is_seller(person):
    return person.is_seller


def BFS(entry):

    searchQ = deque()
    entry.added_to_q = True
    searchQ.append(entry)

    while searchQ:
        person = searchQ.popleft()
        if is_seller(person):
            return person
        else:
            for friend in person.friends:
                if not friend.added_to_q:   # comment this test and it'll create an infinite loop  
                    # This suit should make this version of BFS more efficinet than the one on the book
                    friend.added_to_q = True
                    searchQ.append(friend)

    return None

sami = Person("sami")
naomi = Person("naomi", sami)
sami.friends.append(naomi)
# kiya = Person("kiya")
# yoni = Person("yoni")
# yabse = Person("yabse")

print(BFS(sami))