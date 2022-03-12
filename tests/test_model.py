from datetime import timedelta

from app.api_model import StopsCollection, FilteredStopsCollection
from app.config_db import cur


def test_stops_collection():
    cur.execute("SELECT * FROM bus_stops")
    stops_list = cur.fetchall()

    cur.execute("SELECT * FROM api_key")
    api_key = cur.fetchall()[0][0]
    stops = StopsCollection(api_key, stops_list)

    assert len(stops.stops()) == 3
    assert str(stops.stops()[1]) == "Antka Rozpylacza"


def test_stop_timetable():
    cur.execute("SELECT * FROM bus_stops")
    stops_list = cur.fetchall()

    cur.execute("SELECT * FROM api_key")
    api_key = cur.fetchall()[0][0]
    stop = StopsCollection(api_key, stops_list).stops()[1]
    timetable = stop.timetable()
    assert type(timetable[0][0]) == str
    assert type(timetable[0][1]) == int
    assert type(timetable[0][2]) == str


def test_collection_timetable():
    cur.execute("SELECT * FROM bus_stops")
    stops_list = cur.fetchall()

    cur.execute("SELECT * FROM api_key")
    api_key = cur.fetchall()[0][0]
    stops = FilteredStopsCollection(api_key, stops_list)
    timetable = stops._collection_timetable
    # timetable = stops._timetable_filter_stops([5010, 5099], 20)
    # timetable2 = stops._timetable_time_obj([5010, 5099], 20)
    assert type(timetable[0][0]) == timedelta
    assert type(timetable[0][1]) == int
    assert type(timetable[0][2]) == str


def test_timetable_filter_stops():
    cur.execute("SELECT * FROM bus_stops")
    stops_list = cur.fetchall()

    cur.execute("SELECT * FROM api_key")
    api_key = cur.fetchall()[0][0]
    stops = FilteredStopsCollection(api_key, stops_list)
    timetable = stops._collection_timetable
    assert len(stops._timetable_filter_stops(timetable, [5010])) < len(timetable)


def test_timetable_get():
    cur.execute("SELECT * FROM bus_stops")
    stops_list = cur.fetchall()

    cur.execute("SELECT * FROM api_key")
    api_key = cur.fetchall()[0][0]
    stops = FilteredStopsCollection(api_key, stops_list)
    timetable = stops.get_timetable()
    pass
