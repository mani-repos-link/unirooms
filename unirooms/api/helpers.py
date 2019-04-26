"""
 This python file contains some utility functions.
"""


def get_building_timetable(building: str, feed: list) -> list:
    """
    Finds the timetable of particular building and its rooms
    :param building: can be any letter in range [A-F]
    :param feed: list of feed, where it has to search for it(search space).
    :return: a list of result
    """
    pass


def get_room_timetable(room: str, feed: list) -> list:
    """
    Finds the timetable of particular given room.
    :param room: a room number such as 02, 22, 11, etc. It should have 2 chars
    :param feed: search space
    :return: list of timetable of particular room
    """
    pass


def get_floor_timetable(building: str, floor: str, feed: list) -> list:
    """
    Finds the timetable of all possible rooms that are available at given floor.
    :param building: can be any char in range [A-F]. It will give information, which is the building of floor, we have to look it
    :param floor: floor
    :param feed: search space
    :return: returns a list
    """
    pass


def get_professor_lecture_timetable(professor: str, feed: list) -> list:
    """
    Finds the lecture of professor
    :param professor: professor name
    :param feed:
    :return:
    """
    pass


def get_by_time_timetable(start_time: str, end_time: str, feed: list) -> list:
    """
    Returns the list of all timetable in given datetime
    :param start_time:
    :param end_time:
    :param feed:
    :return: returns a list
    """
    pass



