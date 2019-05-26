"""
 This python file contains some utility functions.
"""
import time
import json
import os
import re

__all__ = [
    "read_json",
    "write_json",
    "get_building_timetable",
    "get_room_timetable",
    "get_floor_timetable",
    "get_professor_lecture_timetable",
    "get_by_time_timetable",
    "get_fresh_timetable_data"
]


def read_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data


def write_json(file_pata, obj):
    with open(file_pata, 'w') as f:
        json.dump(obj, f, indent=4)


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


def get_floor_timetable(building: str, floor: str, feed: list) -> list:
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


def get_professor_lecture_timetable(professor: str, feed: list) -> list:
    """
    Finds the lecture of professor
    :param professor: professor name
    :param feed:
    :return:
    """
    professor = professor.lower()
    if len(feed) == 0:
        return []
    _lectures: List = []
    for lecture in feed:
        if professor in lecture['lecturer'].lower():
            _lectures.append(lecture)
    return _lectures


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
    if start_timestamp is not None and end_timestamp is not None:
        start_timestamp = float(start_timestamp)
        end_timestamp = float(end_timestamp)
        for lecture in feed:
            if lecture['start-timestamp'] >= start_timestamp and lecture["end-timestamp"]<=end_timestamp:
                _lectures.append(lecture)
        return _lectures
    else:
        if start_timestamp is not None:
            start_timestamp = float(start_timestamp)
            for lecture in feed:
                if lecture['start-timestamp'] >= start_timestamp:
                    _lectures.append(lecture)
            return _lectures
        else:
            end_timestamp = float(end_timestamp)
            for lecture in feed:
                if lecture['end-timestamp'] >= end_timestamp:
                    _lectures.append(lecture)
            return _lectures


def get_fresh_timetable_data():
    """
    Returns the fresh time table data by reading from files.
    It add/updates also the lectures in the list.
    Return index:
        - lectures
        - rooms[:room_id]
        - lecturers[:name_lecturer]
        - buildings[:name_building]
        - [buildings][floors][:id]
        - [buildings][room][:id]
        - lecturers_lectures[:name_lecturer]
        - subjects[:lecture_title]
    :return: a list
    """
    lectures = read_json(os.getenv("LECTURES_JSON_FILE"))
    room_data = read_json(os.getenv("ROOMS_JSON_FILE"))
    lecturer_data = read_json(os.getenv("LECTURERS_JSON_FILE"))
    lecturer_data = _update_lecturer_data(lectures, lecturer_data)
    write_json(os.getenv("LECTURERS_JSON_FILE"), lecturer_data)
    return _optimized_data_list(lectures, lecturer_data, room_data)


def _update_lecturer_data(lectures, lecturer_data):
    """
    Finds and updates the professor/lecturer object and returns
    :param lectures: all lecturers object
    :param lecturer_data: old lecturer/professor data
    :return: a list of lecturers object
    """
    dummy_list = {}
    for lect in lectures:
        _lecturer = (re.sub(' +', ' ', lect["lecturer"])).strip()

        if _lecturer not in dummy_list:
            dummy_list[_lecturer] = {
                "is_lect": lect["type"] == "LECT",
                "is_lab": lect["type"] == "LAB" or lect["type"] == 'EXERCISE'
            }
        else:
            if lect["type"] == 'LECT':
                dummy_list[_lecturer]["is_lect"] = True

            if lect["type"] == 'LAB' or lect["type"] == 'EXERCISE':
                dummy_list[_lecturer]["is_lab"] = True

        if _lecturer not in lecturer_data:
            lecturer_data[_lecturer] = {
                "is_lab_teacher": dummy_list[_lecturer]["is_lab"],
                "is_lecturer": dummy_list[_lecturer]["is_lect"],
                "teaching_subjects": [lect["title"]],
            }

        if lect["type"] == "LAB":
            lecturer_data[_lecturer]["is_lab_teacher"] = dummy_list[_lecturer]["is_lab"]

        if lect["type"] == "LECT":
            lecturer_data[_lecturer]["is_lecturer"] = dummy_list[_lecturer]["is_lect"]

        if lect["title"] not in lecturer_data[_lecturer]["teaching_subjects"]:
            lecturer_data[_lecturer]["teaching_subjects"].append(lect["title"])

    return lecturer_data


def _optimized_data_list(lectures, lecturers, rooms):
    """
    Creates a unique list by combining with all other objects such as lectures, lecturers
    :param lectures: list of objects of lectures
    :param lecturers: list of lecturers
    :param rooms: list of all rooms of uni
    :return:
    """
    data = {"lectures": lectures, "rooms": rooms, "lecturers": lecturers}
    buildings = __get_all_buildings_name_list(data["lectures"])

    data["buildings"] = {}
    data["buildings"]["floors"] = {}
    data["buildings"]["rooms"] = {}
    data["lecturers_lectures"] = {}

    for building in buildings:
        data["buildings"][building.upper()] = get_building_timetable(building, data["lectures"])
        building_floors = __get_all_buildings_floors_list(data["buildings"][building])
        for bf in building_floors:
            data["buildings"]["floors"][building+bf] = get_floor_timetable(building, bf, data["buildings"][building])

    for build_floor in data["buildings"]["floors"]:
        rooms = __get_floor_rooms_list(data["buildings"]["floors"][build_floor])
        for room in rooms:
            data["buildings"]["rooms"][build_floor+room] = get_room_timetable(
                build_floor[0],  # building
                build_floor[1],  # floors
                room,  # room number
                data["buildings"]["floors"][build_floor])

    for lect in lectures:
        _lecturer = (re.sub(' +', ' ', lect["lecturer"])).strip()
        if _lecturer in data["lecturers_lectures"]:
            data["lecturers_lectures"][_lecturer].append(lect)
        else:
            data["lecturers_lectures"][_lecturer] = [lect]

    data["subjects"] = __get_all_lecture_titles_list(lectures)
    return data


def __get_all_lecture_titles_list(lectures):
    titles = read_json(os.getenv("LECTURE_TITLES_JSON_FILE"))

    for l in lectures:
        ttl = l["title"]
        if ttl not in titles:
            titles[ttl] = {
                "lecturer": l["lecturer"],
                "type": l["type"],
                "inserted_time": time.time(),
                "last_update": time.time()
            }
        else:
            titles[ttl]["title"] = l["title"]
            titles[ttl]["lecturer"] = l["lecturer"]
            titles[ttl]["type"] = l["type"]
            titles[ttl]["last_update"] = time.time()

    write_json(os.getenv("LECTURE_TITLES_JSON_FILE"), titles)
    return titles


def __get_all_buildings_name_list(lectures):
    buildings = set()
    for l in lectures:
        buildings.add(l["building"])
    return list(buildings)


def __get_all_buildings_floors_list(building_feed):
    buildings_floors = set()
    for l in building_feed:
        buildings_floors.add(l["floor"])
    return list(buildings_floors)


def __get_floor_rooms_list(floor_feed):
    floor_rooms = set()
    for fl_feed in floor_feed:
        floor_rooms.add(fl_feed["room"])
    return list(floor_rooms)





