import requests


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
    def __init__(self, api_key, stops_list):
        self._stops = None
        self._api_key = api_key
        self._process_stops(stops_list)

    def _add_stop(self, stop: BusStop):
        if self._stops is None:
            self._stops = [stop]
        else:
            self._stops.append(stop)

    def _process_stops(self, stops_list):
        for stop in stops_list:
            stop_id = stop[0]
            stop_name = stop[1]
            stop_lines = stop[2]
            stop_nr = stop[3]
            stop_instance = BusStop(stop_id, stop_nr, stop_lines, stop_name)
            self._add_stop(stop_instance)



