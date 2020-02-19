

# Implement a class to hold room information. This should have name and
# description attributes.

# class Room:
#     def __init__(self, name, desc):
#         self.name = name
#         self.desc = desc
#         self.items = []

#         self.n_to = None
#         self.s_to = None
#         self.w_to = None
#         self.e_to = None

##########################################################################

# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None

    def __str__(self):
        '''
        This is a string method
        '''
        return f"{self.title}\n\n{self.description}"
