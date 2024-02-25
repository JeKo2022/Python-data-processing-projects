# MINOR AI
# Assignment: Adventure
# Date: 12 nov. 2021
# Name: Jeanice Koorndijk

#  To be able to access the Room class from the adventure.py file, we use import
from room import Room


class Adventure():
    '''
    class executes game like moving around. It does not print or get input from player directly, only on basis of main class.
    it calls only on Room class.
    '''

    # Create rooms and items for the appropriate 'game' version.
    def __init__(self, game):
        '''
        Function initializes the dictionary self.rooms in which the rooms and room objects will be stored.
        It also reads correct file, also does an assertion.
        '''

        # Rooms is a dictionary that maps a room number to the corresponding room object
        self.rooms = {}

        # Load room structures
        self.load_rooms(f"data/{game}Adv.dat")

        # Game always starts in room number 1, so we'll set it after loading
        assert 1 in self.rooms
        self.current_room = self.rooms[1]

    # Load rooms from filename in two-step process
    def load_rooms(self, filename):
        '''
        Function reads the file line by line.
        paragraph 1: info is added to self.rooms (dictionary).
        paragraph 2: appropriate connections are made to each room in each dictionry for connections.
        '''

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

                    # read a line using
        #             for i in range(2):
                    # line = f.readline()

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

                # paragraph 2: make connections
                if counter_newparagraphs == 1 and line != '\n':

                    # set empty lists for all directions and correpsonding rooms
                    l_directions = []
                    l_rooms = []

                    # prep line to loop over every line with rooms and directions for particular room
                    line = line[:-1].strip().split("\t")

                    # add the  directions to seperate lists for particular room (for later use in dictionary)
                    for direction in range(1, len(line), 2):
                        l_directions.append(line[direction])

                    # add the rooms to seperate lists for particular room (for later use in dictionary)
                    for room in range(2, len(line), 2):
                        room_number = int(line[room])
                        linked_room = self.rooms[room_number]
                        l_rooms.append(linked_room)

                    # add the rooms and directions to dictionary for particular room using add_connections
                    for i in range(len(l_directions)):

                        # set source room to desired room of current line
                        room_id = int(line[0])
                        source_room = self.rooms[room_id]

                        # add connections to room
                        source_room.add_connection(l_directions[i], l_rooms[i])

                assert 1 in self.rooms
                assert self.rooms[1].name == "Outside building"

    # Pass along the description of the current room
    def get_description(self):
        '''
        Function passes along the description of the current room.
        '''

        # if room visited before, short name passed along
        if self.current_room.already_visited() == True:
            name = self.current_room.name
            return name

        # if room not visited before, long description passed along
        else:
            description = self.current_room.description

            # if room not visited before, note that the room has been visited
            visited = self.current_room.set_visited()
            return description

    # Move to a different room by changing "current" room, if possible
    def move(self, direction):
        '''
        This function allows moving around.
        It returns a boolean True or False depending on whether the move was possible.
        The main program can also use this result to notify the user if the move could not be performed.
        '''

        # move if it is possible to move in the desired direction
        if self.current_room.has_connection(direction):
            self.current_room = self.current_room.get_connection(direction)
            return True

        # returns false if it is not possible to move in desired direction: "invalid command"
        else:
            return False

    def get_long_description(self):
        '''
        This function always returns the long description.
        For use when player enters "LOOK".
        '''

        self.long_description = self.current_room.description
        return self.long_description

    def forced(self):
        '''
        This function checks wether a player is in a room that has a direction named FORCED.
        The output is used to implement the feature "forced movement" in main.
        '''

        if 'FORCED' in self.current_room.connections:
            return True
        else:
            return False


if __name__ == "__main__":
    '''
    Main function that performs the game. Calls only on adventure class not room.
    Executes all prints.
    '''

    from sys import argv

    # Check command line arguments
    if len(argv) not in [1, 2]:
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

    # synonyms: create dictionary for valid commands
    synonyms = {}

    # read synonyms file
    with open("data/Synonyms.dat", "r") as s:

        # create a loop to read the room data:
        for line in s:
            line = line.strip().split("=")
            synonyms[line[0]] = line[1]

    # Prompt the user for commands until they type QUIT
    while True:

        # Prompt
        command = input("> ").lower()

        # set command to upper for comparison with standard data
        command = command.upper()

        # check wether command in synonyms and set command to appropriate command.
        if command in synonyms:
            command = synonyms[command]

        # check for additional command (help, quit, look):
        additional_command = command

        # Escape route
        if additional_command == "QUIT":
            break

        elif additional_command == "HELP":
            print("You can move by typing directions such as EAST/WEST/IN/OUT\n""QUIT quits the game.\n"
                  "HELP prints instructions for the game.\n""LOOK lists the complete description of the room and its contents.\n")

        elif additional_command == "LOOK":
            print(adventure.get_long_description())

        # pass the entered command to the adventure class’s move method.
        elif adventure.move(command) == True:

            # display the room description after each command, so it feels like moving around in the map.
            print(adventure.get_description())

        elif adventure.move(command) == False:
            print("Invalid command")

        # Forced movement
        if adventure.forced() == True:

            # the long room description will be printed (even if already visited)
            print(adventure.get_long_description())

            # set command to forced for execution of forced movement
            command = "FORCED"

            # execute forced movement
            adventure.move(command)

            # print(long or short description)
            print(adventure.get_description())
