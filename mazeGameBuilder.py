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


class MazeBuilder():
    def __init__(self):
        pass

    def build_room(self, rN):
        pass

    def build_door(self, r1, r2):
        pass

    def build_maze(self):
        pass

    def get_maze(self):
        return None


class MazeGame():
    def create_maze(self, builder):
        builder.build_maze()
        builder.build_room(1)
        builder.build_room(2)
        builder.build_door(1, 2)

        return builder.get_maze()

    def create_complex_maze(self, builder):
        builder.build_room(1)
        builder.build_room(1001)

        return builder.get_maze()


class Interface_StanderMazeBuilder(MazeBuilder):


    def __init__(self):
        pass

    def build_room(self, rN):
        pass

    def build_door(self, r1, r2):
        pass

    def build_maze(self):
        pass

    def get_maze(self):
        return Maze

    def common_wall(self, r1, r2):
        return Direction
    _currentMaze = Maze


class StanderMazeBuilder(MazeBuilder):
    def __init__(self):
        self._currentMaze = None

    def build_maze(self):
        self._currentMaze = Maze()

    def build_room(self, rN):
        try:
            self._currentMaze.get_room_number(rN)
        except:
            print("  this room does not exist   ....  creating it  ")
            room = Room(rN)
            self._currentMaze.set_room(room)

            room.set_side(Direction.North.value, Wall())
            room.set_side(Direction.South.value, Wall())
            room.set_side(Direction.East.value, Wall())
            room.set_side(Direction.West.value, Wall())

    def build_door(self, r1, r2):
        room1 = self._currentMaze.get_room_number(r1)
        room2 = self._currentMaze.get_room_number(r2)

        door = Door(room1, room2)

        room1.set_side(self.common_wall(room1, room2), door)
        room2.set_side(self.common_wall(room2, room1), door)

        for side in range(4):
            if 'Door' in str(room1._sides[side]):
                print('Room1: ', room1._sides[side], Direction(side))
            if 'Door' in str(room2._sides[side]):
                print('Room2: ', room2._sides[side], Direction(side))

    def get_maze(self):
        return self._currentMaze

    def common_wall(self, aRoom, anotherRoom):
        if aRoom._roomNumber < anotherRoom._roomNumber:
            return Direction.East.value
        else:
            return Direction.West.value



if __name__ == '__main__':
    print("*" * 21)
    print("***  the game will start  ***")
    print("*" * 21)

    maze = Maze
    game = MazeGame()
    builder = StanderMazeBuilder()

    game.create_maze(builder)
    maze = builder.get_maze()
