<img width="64" height="38" alt="owf" src="https://github.com/user-attachments/assets/2155b8c4-86c4-4292-9aca-f251774982d9" />

# open-weather-fetch

Open Weather Fetch is a collection of scripts that fetch local weather and
store the result in a json file. It also downloads icon representations of
the weather conditions.

This is so clients on the system can instantly have real time weather data
without having to connect to the network servers and download the data,
it is already on the file system.

This means that multiple clients can use the data instantly without
worrying about weather service usage limits and the caveats of configuring
weather services and connecting to the network.

## Configuration

### OpenWeatherMap

OpenWeatherMap Free API Key Signup

1) Navigate to https://home.openweathermap.org/users/sign_up

2) Fill out the form

3) Complete the captcha

4) Click Create Account button

5) Check email and verify account

6) Wait about 2 hours for the key to become active

7) Navigate to https://home.openweathermap.org/api_keys

8) Copy the Default API key for use

9) Install the API key into ~/.config/owf/config.json using example_config.json as a template

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
