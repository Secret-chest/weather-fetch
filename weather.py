import locale
import json
import os
import importlib
import traceback
import sys
from datetime import datetime
from pathlib import Path
from gi.repository import GLib, Gio, GObject

def load_packages_from_dir(dir_path: Path):
    loaded_modules = []
    for path in dir_path.iterdir():
        if path.name.startswith("_"):
            continue
        if path.is_dir() and (path / "__init__.py").exists():
            try:
                module_name = path.name
                spec = importlib.util.spec_from_file_location(module_name, path / "__init__.py")
                module = importlib.util.module_from_spec(spec)
                module.__package__ = module_name
                sys.modules[module_name] = module
                spec.loader.exec_module(module)
                loaded_modules.append(module)
            except Exception as e:
                print(f"{datetime.now().strftime('[%H:%M:%S]')} Failed to load weather module {path.name}: {e}", file=sys.stderr)
                traceback.print_exc()
        else:
            continue
    return loaded_modules


class WeatherUpdater(Gio.Application):
    def __init__(self):
        super().__init__(
            application_id="com.roundabout_host.roundabout.PanoramaIndicatorService",
            flags=Gio.ApplicationFlags.FLAGS_NONE,
        )

        self.config_path = Path(os.environ.get("XDG_CONFIG_HOME") or "~/.config").expanduser() / "weather" / "config.json"
        self.fetcher_paths = ([Path(os.environ.get("XDG_DATA_HOME") or "~/.local/share").expanduser() / "weather" / "fetchers"]
                              + ([Path(p) / "fetchers" for p in os.environ.get("XDG_DATA_DIRS").split(":")] if "XDG_DATA_DIRS" in os.environ
                                else [Path("/") / "usr" / "share" / "fetchers"]))
        self.data_path = Path(os.environ.get("XDG_DATA_HOME") or "~/.local/share").expanduser() / "weather" / "data"

        self.modules_list = []

        for path in self.fetcher_paths:
            if path.is_dir():
                self.modules_list += load_packages_from_dir(path)

        self.modules = {}
        for module in self.modules_list:
            self.modules[module.__name__] = module

        print(self.modules)

        with open(self.config_path, "r") as f:
            data = json.load(f)
            (self.data_path / "locations").mkdir(parents=True, exist_ok=True)
            # Create the symlink
            if (self.data_path / "data.json").exists():
                (self.data_path / "data.json").unlink()
            os.symlink(self.data_path / "locations" / f"{data['main_location']}.json", self.data_path / "data.json")
            for i, location in enumerate(data["locations"]):
                module = self.modules[location["source"]]
                settings = location.copy()
                del settings["source"], settings["interval"]
                module.fetch_weather(**settings, i=i)

                GLib.timeout_add_seconds(location["interval"], lambda: module.fetch_weather(**settings) or True)

                print(f"{datetime.now().strftime('[%H:%M:%S]')} Downloaded weather data for {location["location"]}")

    def do_startup(self):
        Gio.Application.do_startup(self)

    def do_activate(self):
        self.hold()

    def do_shutdown(self):
        Gio.Application.do_shutdown(self)


if __name__ == "__main__":
    app = WeatherUpdater()
    app.run()
