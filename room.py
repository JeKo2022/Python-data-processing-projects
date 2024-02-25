# MINOR AI
# Assignment: Room


class Room ():
    '''
    class keeps track of objects of each room.
    '''

    def __init__(self, room_id, name, description):
        '''
        Function does some initializing
        '''

        # store information about the room itself
        self.room_id = room_id
        self.name = name
        self.description = description

        # set empty dictionary for storing information about the connections
        self.connections = {}

        # set attribute give a short description if player enters a room they’ve already seen.
        self.visited = False

    def add_connection(self, direction, destination_room):
        '''
        accepts a direction (string) and a room (another Room object), and stores those in the dictionary
        '''

        self.connections[direction] = destination_room
        return self.connections[direction]

    def has_connection(self, direction):
        '''
        accepts a direction (string), and checks whether there is a connection in the dictionary under that name
        '''

        return direction in self.connections

    def get_connection(self, direction):
        '''
        accepts a direction (string), and retrieves the actual Room object that it connects to
        '''

        return self.connections[direction]

    def set_visited(self):
        '''
        function sets attribute visited to true when room is visited for later use in already visited
        '''

        self.visited = True
        return self.visited

    def already_visited(self):
        '''
        function considers whether room has been visited before by player
        can beused to determine whether short or long description should be printed
        '''

        # give a short description if player enters a room they’ve already seen
        if self.visited == True:
            return True
        else:
            return False
