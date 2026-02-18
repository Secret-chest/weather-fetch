# open-weather-fetch

Open Weather Fetch is a collection of scripts that fetch local weather and
store the result in a json file. It also downloads icon representations of
the weather conditions.

This is so clients on the system can instantly have real time weather data
without having to connect to the network servers and download the data,
it is already on the file system.

This means that multiple clients can use the data instantly without
worrying about weather sevice usage limits and the caveats of configuring
weather services and connecting to the network.

## Installation

`git clone https://github.com/Secret-chest/open-weather-fetch`

`cd open-weather-fetch`

`meson setup -Dsystemd_prefix=/usr/lib --prefix=/usr build`

`sudo -E ninja -C build install`

`systemctl --user daemon-reload`

`systemctl --user enable open-weather-fetch`

`systemctl --user start open-weather-fetch`

## Verification

Check the status after enabling the service to ensure everything went ok:

`systemctl --user status open-weather-fetch`

Make sure the fetched data is in the expected location:

`ls -l ~/.local/share/owf/data/data.json`
