import requests
import json


class BusStop:
    def __init__(self):
        self._stop_id = None
        self._stop_nr = None
        self._lines = None
        self._name = None

    def __str__(self):
        return self._name


class StopsCollection:
    def __init__(self):
        self._stops = None
        self._api_key = None

    def _set_up_api_key(self):
        pass

    def _add_stop(self, stop: BusStop):
        if self._stops is None:
            self._stops = [stop]

    def _fetch_request(self, url):
        return requests.get(url).json()

    def _make_request(self, stop_id, stop_nr, line, api_key):
        url = f"https://api.um.warszawa.pl/api/action/dbtimetable_get/?id=e923fa0e-d96c-43f9-ae6e-60518c9f3238&busstopId={stop_id}&busstopNr={stop_nr}&line={line}&apikey={api_key}"
        return self._fetch_request(url)

    def _get_stops_data(self, api_key):
        url = f"https://api.um.warszawa.pl/api/action/dbstore_get?id=1c08a38c-ae09-46d2-8926-4f9d25cb0630&apikey={api_key}"
        return self._fetch_request(url)

    def parse_stops_data(self, path):
        data = self._get_stops_data(path)
        pass


if __name__ == "__main__":
    stops = StopsCollection()
    stops.parse_stops_data()
