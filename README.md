# open-weather-fetch

This is a JSON file format for weather data to be downloaded in, to be used by
various weather clients, primarily on GNU/Linux systems.

The project offers a backend/frontend split, making it so the weather backends
periodically save updated weather data to a file. Then, the various weather
clients one desires to use can all have recent weather information without
having to make requests themselves, and allowing the user to choose their
desired weather source independently of the display software.

Weather data is stored in JSON, in `~/.local/share/weather/data/`. To see the
weather JSON spec, refer to `data_file_spec.md` in this repository.

In that directory, a `data.json` file is the main weather file. In the future,
it will be possible to have a subdirectory `locations` with more weather files
for other locations, keeping `data.json` for the current one. That is, a small
weather client such as a panel applet can read just `data.json`, whereas a
windowed weather app might want to read all cities.

## Downloading weather data

Just run the provided `weather.py` after putting the `fetchers` in
`~/.local/share/weather/fetchers` and the config in
`~/.config/weather/config.json`. The fetchers can also be in
`/usr/share/weather/fetchers` if you want to install this system-wide.

## Installation

You can use the provided `weather.service` as a user unit for systemd and put
the fetchers in `/usr/share/weather/fetchers`, and the `weather.py` in
`/usr/bin/weather-fetch.py`. Enable the user unit, and it should run.
