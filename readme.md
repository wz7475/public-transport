# Public transport service

## Brief summary
Service made with **Python, Flask, PostgreSQL, React** to use personal timetable for public transport.

## Idea
It was common situation in the morning when I had to check in hurry timetable for 2 bus stops and 1 tram stop to choose best connection to my faculty. It demanded checking 3 stops and filtering out proper lines. Public transport apps like Google Maps or "Jak dojade" were insufficient, they didn't show some fastest connections and cluttered output with slow/way around options.

So  decided to create service showing only my desired connections. 

## Implementation
Chosen lines and stops are stored in PostgreSQL database. They're processed by backend in Flask which retrieves timetable from https://api.um.warszawa.pl/ this external api. Frontend is made with React.js. App is during development. App will have options to:
* create custom sets of stops and lines (gui for storing data in database)
* choose go out time
* filters for certain stops