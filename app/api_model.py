from datetime import datetime, timedelta

import pytz as pytz
import requests


def str_date_to_timedelta(time_str):
    datetime_obj = datetime.strptime(time_str, "%H:%M:%S")
    delta = timedelta(
        hours=datetime_obj.hour,
        minutes=datetime_obj.minute,
        seconds=datetime_obj.second
    )
    return delta


class BusStop:
    def __init__(self, stop_id, stop_nr, stop_lines, stop_name, api_key):
        self._stop_id = stop_id
        self._stop_nr = stop_nr
        self._lines = stop_lines
        self._name = stop_name
        self._api_key = api_key
        self._timetable = None

    def id(self):
        return self._stop_id

    def timetable(self):
        self._fetch_timetable()
        return self._timetable

    def _fetch_request(self, url):
        return requests.get(url).json()

    def _make_request(self, line):
        url = (
            f"https://api.um.warszawa.pl/api/action/dbtimetable_get"
            f"?id=e923fa0e-d96c-43f9-ae6e-60518c9f3238&busstopId={self._stop_id}"
            f"&busstopNr={self._stop_nr}&line={line}&apikey={self._api_key}"
        )
        return self._fetch_request(url)

    def _fetch_timetable_per_line(self, line):
        json_dict = self._make_request(line)
        for time_obj_list in json_dict["result"]:
            time_delta = str_date_to_timedelta(time_obj_list["values"][5]["value"])
            position = time_delta, line, self._name, self._stop_id
            if self._timetable is None:
                self._timetable = [position]
            else:
                self._timetable.append(position)

    def _fetch_timetable(self):
        for line in self._lines:
            self._fetch_timetable_per_line(line)

    def __str__(self):
        return self._name


class StopsCollection:
    """base class to set up stops objects"""

    def __init__(self, api_key, stops_list):
        self._stops = None
        self._api_key = api_key
        self._process_stops(stops_list)
        self._collection_timetable = None

    def _filter_stops(self, stops_ids):
        stops_buffer = []
        for stop in self._stops:
            if stop.id() in stops_ids:
                stops_buffer.append(stop)
        return stops_buffer

    def _process_timetable(self, filtered_stops):
        """set collection_timetable as a timetable for all stops"""
        # reset before next fetch
        self._collection_timetable = None
        for stop in filtered_stops:
            if self._collection_timetable is None:
                self._collection_timetable = stop.timetable()
            else:
                self._collection_timetable += stop.timetable()

    def stops(self):
        return self._stops

    def _add_stop(self, stop: BusStop):
        if self._stops is None:
            self._stops = [stop]
        else:
            self._stops.append(stop)

    def _process_stops(self, stops_list):
        """create initial stop list"""
        for stop in stops_list:
            stop_id = stop[0]
            stop_name = stop[1]
            stop_lines = stop[2]
            stop_nr = stop[3]
            stop_instance = BusStop(
                stop_id, stop_nr, stop_lines, stop_name, self._api_key
            )
            self._add_stop(stop_instance)


class FilteredStopsCollection(StopsCollection):
    """class for processing/filtering timetable

    - constructing instance - fetch and process timetable for all stops and save it as attribute
            (takes longer time -> waiting for external api of WTP)
    - get_timetable - filter timetable fetched at constructing object and return desired data
    """

    def __init__(self, api_key, stop_list):
        super().__init__(api_key, stop_list)
        # initialize timetable for all stops -> to filter later on
        self._process_timetable(self._stops)
        self._filtered_timetable = None

    @staticmethod
    def _timetable_filter_stops(timetable, stops_ids):
        """filter given timetable"""
        filtered_timetable = []
        for position in timetable:
            if position[3] in stops_ids:
                filtered_timetable.append(position)
        return filtered_timetable

    @staticmethod
    def _timetable_sort_time(timetable, time_delta):
        """filter given timetable, return tuple with past and future timetables"""
        # time_delta = str_date_to_timedelta(time_str)
        past_timetable = []
        future_timetable = []
        for position in timetable:
            if position[0] < time_delta:
                past_timetable.append(position)
            else:
                future_timetable.append(position)
        past_timetable.sort(key=lambda pos: pos[0])
        future_timetable.sort(key=lambda pos: pos[0])
        return past_timetable, future_timetable

    def get_timetable(self, stops_ids=None, time=None, amount=35):
        """class api to get timetable with filters"""
        if stops_ids is not None:
            filtered_stops_timetable = self._timetable_filter_stops(self._collection_timetable, stops_ids)
        else:
            filtered_stops_timetable = self._collection_timetable
        if time is not None:
            time_delta = str_date_to_timedelta(time)
        else:
            time_delta = self._get_current_time()
        past_timetable, future_timetable = self._timetable_sort_time(filtered_stops_timetable, time_delta)
        if len(past_timetable) < 5:
            final_timetable = past_timetable
        else:
            final_timetable = past_timetable[:5]
        future_positions_amount = amount - len(final_timetable)
        if len(future_timetable) < future_positions_amount:
            final_timetable += future_timetable
        else:
            final_timetable += future_timetable[:future_positions_amount]
        return final_timetable

    @staticmethod
    def _get_current_time():
        pl_time_zone = pytz.timezone("Poland")
        now = datetime.now(pl_time_zone)
        return timedelta(
            hours=now.hour,
            minutes=now.minute,
            seconds=now.second
        )
