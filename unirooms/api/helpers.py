"""
 This python file contains some utility functions.
"""
import time


def get_building_timetable(building: str, feed: list) -> list:
    """
    Finds the timetable of particular building and its rooms
    :param building: can be any letter in range [A-F]
    :param feed: list of feed, where it has to search for it(search space).
    :return: a list of result
    """
    if len(feed) == 0:
        return []
    lectures: List = []
    for lecture in feed:
        if lecture['building'] != building:
            continue
        lectures.append(lecture)
    return lectures


def get_room_timetable(building: str, floor: str, room: str, feed: list) -> list:
    """
    Finds the timetable of particular given room.
    :param building: a building, in which you want to search the room.
    :param floor: the floor in which you want to search the room
    :param room: a room number such as 02, 22, 11, etc. It should have 2 chars
    :param feed: search space
    :return: list of timetable of particular room
    """
    if len(feed) == 0:
        return []
    lectures: List = []
    for lecture in feed:
        if lecture['building'] == building and lecture["floor"] == floor and lecture['room'] == room:
            lectures.append(lecture)
    return lectures


def get_floor_timetable(building: str, floor: str,  feed: list) -> list:
    """
    Finds the timetable of all possible rooms that are available at given floor.
    :param building: can be any char in range [A-F]. It will give information,
    which is the building of floor, we have to look it
    :param floor: floor
    :param feed: search space
    :return: returns a list
    """

    if len(feed) == 0:
        return []
    lectures: List = []
    for lecture in feed:
        if lecture['building'] == building and lecture["floor"] == floor:
            lectures.append(lecture)
    return lectures


def get_professor_lecture_timetable(professor: str, feed: list) -> list:
    """
    Finds the lecture of professor
    :param professor: professor name
    :param feed:
    :return:
    """
    pass


def get_by_time_timetable(start_timestamp: float, end_timestamp: float, feed: list) -> list:
    """
    Returns the list of all timetable in given datetime
    :param start_timestamp: start time
    :param end_timestamp: end time
    :param feed: feed of lectures
    :return: returns a list
    """
    if len(feed) == 0:
        return []
    _lectures: List = []
    for lecture in feed:
        if lecture['start-timestamp'] >= float(start_timestamp) and lecture["end-timestamp"] <= float(end_timestamp):
            _lectures.append(lecture)
    return _lectures



