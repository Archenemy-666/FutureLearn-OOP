class Room():
    def __init__(self,room_name):
        self.name = room_name
        self.description=None
        self.linked_rooms = {}

    def set_description(self,room_description):
        self.description = room_description

    def get_description(self):
        return self.description 

    def set_name(self,room_name):
        self.name = room_name

    def get_name(self):
        return self.name

# do not repeat the attributes such as def description it overlays to an error (important)
    def describe(self):
        print(self.description)

    #create an empty dictionary in the initialization   
    def link_room(self,room_to_link,direction):
        self.linked_rooms[direction] = room_to_link
        print( self.name + " linked rooms :" + repr(self.linked_rooms))
# the below doesnt work with class in print statement another attribute to call room names must be created
    def get_details(self):
        print("\n")
        print(self.get_name())
        print("----------------------------------------")
        print(self.get_description())
        for direction in self.linked_rooms :
            room = self.linked_rooms[direction]
            print("the " +room.get_name() + " is " + direction)
        print("=================================")
    
    def move(self,direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("room not found")
            return self

