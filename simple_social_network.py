"""A simple social network for tracking connections between poeple."""


class Person: 
    """A person in the social network.
    
    Attributes:
        name (str): the person's name
        connetions (set of Person): other people in the social network who know
            this person.
    """
    
    
    def __init__(self, name):
        """Initialize a new Person object."""
        self.name = name
        self.connections = set()
        
        
def connect(self, person2):
    """Connect with person2.
    
    Args:
        person2 (Person): the other person to connect to.
    """
    