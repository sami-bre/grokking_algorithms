class Person:
    def __init__(self, name, *args):
        self.name = name
        self.friends = []
        self.mango_seller = False
        for arg in args:
            self.friends.append(arg)

    def __repr__(self):
        return self.name


nick = Person("nick")
nick.mango_seller = True

sami = Person(
    "sami",
    Person(
        "Alice",
        Person("Peggy")
    ),
    Person(
        "Bob",
        Person("Anuj"),
        nick
    ),
    Person(
        "Clarie",
        Person("Thon"),
        Person("Jonny"),
    )
)




def BFS(person):
    """Performs a breadth first search to find oif there is a mango seller in the graph.
    if not found, returns None"""
    if person.mango_seller:
        return person

    people = []
    for friend in person.friends:
        people.append(friend)

    for p in people:
        if p.mango_seller:
            return p
        else:
            people.extend(p.friends)
    
    return None

print(BFS(sami))
    
