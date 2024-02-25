#  To be able to access the Room class from the adventure.py file, we use import
from roompractice import Room

class Adventure():
    #  contains all methods that make the game work.

    # Create rooms and items for the appropriate 'game' version.
    def __init__(self, game):

        # Rooms is a dictionary that maps a room number to the corresponding room object
        self.rooms = {}

        # Load room structures
        self.load_rooms(f"data/{game}Adv.dat")

        # Game always starts in room number 1, so we'll set it after loading
        assert 1 in self.rooms
        self.current_room = self.rooms[1]

    # Load rooms from filename in two-step process
    def load_rooms(self, filename):
        # TODO

        # read file
        with open(filename) as f:

            # set counter to keep track of paragraphs
            counter_newparagraphs = 0

            # create a loop to read the room data:
            for line in f:

                # keep track of new lines that indicate a new paragraph
                if line == '\n':
                    counter_newparagraphs += 1

                # first paragraph: creating rooms
                if counter_newparagraphs == 0 and line != '\n':

                    # split() it into a list, making sure you split on the TAB character (“\t”)
                    # remove "\n" at the end of the line and split line into seperate characters to work with seperate strings
                    line = line[:-1].split("\t")

                    # set variables to add to room object
                    room_id = int(line[0])
                    name = line[1]
                    description = line[2]

                    # create a new room object using the data from the list
                    room = Room(room_id, name, description)

                    # add room to self.rooms for later use
                    self.rooms[room_id] = room

                assert 1 in self.rooms
                assert self.rooms[1].name == "Outside building"


    # Pass along the description of the current room
    def get_description(self):
        # TODO
        pass

    # Move to a different room by changing "current" room, if possible
    def move(self, direction):
        # TODO
        pass


if __name__ == "__main__":

    from sys import argv

    # Check command line arguments
    if len(argv) not in [1,2]:
        print("Usage: python adventure.py [name]")
        exit(1)

    # Load the requested game or else Tiny
    if len(argv) == 1:
        game_name = "Tiny"
    elif len(argv) == 2:
        game_name = argv[1]

    # Create game
    adventure = Adventure(game_name)

    # Welcome user
    print("Welcome to Adventure.\n")

    # Print very first room description
    print(adventure.get_description())

    # Prompt the user for commands until they type QUIT
    while True:

        # Prompt
        command = input("> ").lower()

        # Perform move or other command
        # TODO

        # Escape route
        if command == "quit":
            break
