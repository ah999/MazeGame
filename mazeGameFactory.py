from enum import Enum
from builtins import classmethod

class MapSide():

    def enter(self):
        raise NotImplementedError('Doesn"t implemented yet')


class Direction(Enum):
    North = 0
    South = 1
    East = 2
    West = 3


class Room(MapSide):

    def __init__(self, roomNo):
        self._roomNumber = int(roomNo)
        self._sides = [MapSide]*4

    def enter(self):
        print("***** you've just entered the room *****   ")

    def set_side(self, Direction, MapSide):
        self._sides[Direction] = MapSide

    def get_side(self, Direction):
        return self._sides[Direction]


class Wall(MapSide):

    def enter(self):
        print(" * it's a wall watch your head!! * ")


class Door(MapSide):

    def __init__(self, Room1=None, Room2=None):
        self._room1 = Room1
        self._room2 = Room2
        self._isOpen = False

    def enter(self):
        if self._isOpen == True: print("***  the door is open you can pass over!!  *** ")
        else: print("* you need to open the door first to pass!! * ")

    def other_side(self, Room):
        print("this door is a side of a room number: {} ".format(Room._roomNumber))
        if 1 == Room._roomNumber:
            other_room = self._room2
        else:
            other_room = self._room1
        return other_room


class Maze():

    def __init__(self):
        self._rooms = {}

    def set_room(self, room):
        self._rooms[room._roomNumber] = room

    def get_room_number(self, room_number):
        return self._rooms[room_number]


class MazeFactory():
    @classmethod
    def make_maze(cls):
        return Maze()

    @classmethod
    def make_wall(cls):
        return Wall()

    @classmethod
    def make_door(cls, r1, r2):
        return Door(r1, r2)

    @classmethod
    def make_room(cls, rN):
        return Room(rN)


class Spell():

    def __repr__(self):
        return "a hard coded spell !!     "

class EnchantedDoor(Door):

    def __init__(self, r1, r2):
        super(EnchantedDoor, self).__init__(r1, r2)
        self.spell = Spell()

    def enter(self):
        print("****   this door needs a spell   ****", self.spell)
        if self._isOpen == True:
            print("***  the door is open you can pass over!!  *** ")
        else:
            print("* you need to open the door first to pass!! * ")

class EnchantedRoom(Room):
    def __init__(self, roomNo, aSpell):
        super(EnchantedRoom, self).__init__(roomNo)
        print("the spell is ", aSpell)


class EnchantedMazeFactroy(MazeFactory):

    @classmethod
    def cast_spell(cls):
        return Spell()

    @classmethod
    def make_door(cls, r1, r2):
        return EnchantedDoor(r1, r2)

    @classmethod
    def make_room(cls, n):
        return EnchantedRoom(n, cls.cast_spell())

class MazeGame():

    def create_maze(self, factory=MazeFactory):

        maze = factory.make_maze()
        room1 = factory.make_room(1)
        room2 = factory.make_room(2)
        door = factory.make_door(room1, room2)

        # maze creation
        maze.set_room(room1)
        maze.set_room(room2)

        # Creating room 1
        room1.set_side(Direction.North.value, factory.make_wall())
        room1.set_side(Direction.South.value, factory.make_wall())
        room1.set_side(Direction.East.value, door)
        room1.set_side(Direction.West.value, factory.make_wall())

        # Creating room2
        room2.set_side(Direction.North.value, factory.make_wall())
        room2.set_side(Direction.South.value, factory.make_wall())
        room2.set_side(Direction.East.value, factory.make_wall())
        room2.set_side(Direction.West.value, door)


        return maze

if __name__ == '__main__':

    def find_maze_rooms(maze_obj):
        maze_rooms = []
        for room_number in range(4):
            try:
                room = maze_obj.get_room_number(room_number)
                print("*** maze has {} rooms  ***".format(room_number, room))
                print("**** entering the room ........>  ****")
                room.enter()
                maze_rooms.append(room)
                for side in range(4):
                    current_side = room.get_side(side)
                    side_str = str(current_side.__class__).replace("<class '__main__.", "").replace("'>", "")
                    print('    Room: {}, {:<15s}, Type: {}'.format(room_number, Direction(side), side_str))
                    print('    Trying to enter: ', Direction(side))
                    current_side.enter()
                    if 'Door' in side_str:
                        door = current_side
                        if not door._isOpen:
                            print("****  the door is opening ..... ****")
                            door._isOpen = True
                            door.enter()

                        print(door)
                        other_room = door.other_side(room)
                        print("***  on the other side room {}  ***".format(other_room._roomNumber))
                        break



            except KeyError:
                print("no room ",room_number)
        room_numbers = len(maze_rooms)
        print("the maze has {} rooms".format(room_numbers))
        print("########  end of game  ########")


    print("*"*21)
    print("***  the game will start  ***")
    print("*"*21)

    factory = MazeFactory
    print(factory)

    maze_obj = MazeGame().create_maze(factory)
    find_maze_rooms(maze_obj)

    print("*"*21)
    print("***  the game will start  ***")
    print("*"*21)

    factory = EnchantedMazeFactroy
    print(factory)

    maze_obj = MazeGame().create_maze(factory)
    find_maze_rooms(maze_obj)
