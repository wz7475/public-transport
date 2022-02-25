import requests
import json


class BusStop:
    def __init__(self, stop_id, stop_nr, stop_lines, stop_name):
        self._stop_id = stop_id
        self._stop_nr = stop_nr
        self._lines = stop_lines
        self._name = stop_name

    def _fetch_request(self, url):
        return requests.get(url).json()

    def _make_request(self, stop_id, stop_nr, line):
        url = f"https://api.um.warszawa.pl/api/action/dbtimetable_get/?id=e923fa0e-d96c-43f9-ae6e-60518c9f3238&busstopId={stop_id}&busstopNr={stop_nr}&line={line}&apikey={self._api_key}"
        return self._fetch_request(url)

    def __str__(self):
        return self._name


class StopsCollection:
    def __init__(self):
        self._stops = None
        self._api_key = None
        self._set_up_api_key()
        self._process_stops()

    def _set_up_api_key(self):
        with open("app/secrets.json") as f:
            apikey_dict = json.load(f)
        self._api_key = apikey_dict["api_key"]

    def _add_stop(self, stop: BusStop):
        if self._stops is None:
            self._stops = [stop]
        else:
            self._stops.append(stop)

    def _get_stops_data(self):
        with open("app/config.json") as f:
            stops_dict = json.load(f)
        return stops_dict

    def _process_stops(self):
        stops = self._get_stops_data()
        for stop in stops:
            pass
            stop_id = stop
            stop_name = stops[stop]["name"]
            stop_nr = stops[stop]["stop_nr"]
            stop_lines = stops[stop]["lines"]
            stop_instance = BusStop(stop_id, stop_nr, stop_lines, stop_name)
            self._add_stop(stop_instance)


def get_stops_data():
    pass


if __name__ == "__main__":
    stops = StopsCollection()
    stops.parse_stops_data()
