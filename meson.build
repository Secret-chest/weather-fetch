project(
    'open-weather-fetch',
    version: '0.1.0',
)

# Main Python module
install_data(
    'weather.py',
    install_dir: join_paths(get_option('prefix'),
    get_option('bindir')),
    rename: 'open-weather-fetch',
    install_mode: 'rwxr-xr-x'
)

# Systemd unit
conf = configuration_data()
conf.set('prefix', get_option('prefix'))
conf.set('systemd_prefix', get_option('systemd_prefix'))
conf.set('bindir', join_paths(get_option('prefix'), get_option('bindir')))

service_file = configure_file(
    input: 'open-weather-fetch.service',
    output: 'open-weather-fetch.service',
    configuration: conf,
    install: true,
    install_dir: join_paths(get_option('systemd_prefix'), 'systemd', 'user')
)

# Fetchers
install_subdir(
    'fetchers',
    install_dir: join_paths(join_paths(get_option('prefix'), get_option('datadir')), 'owf')
)
