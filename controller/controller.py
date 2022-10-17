import os
from PIL import ImageTk, Image
from view.view import View
from model.weather import Weather
from model.mapbox import MapBox


class Controller:

    def __init__(self) -> None:
        self.update_icon = None
        self.view = View(self)
        self.weather = Weather()
        self.mapbox = MapBox()

        self.update_gui()

    def main(self):
        self.view.main()

    def update_gui(self):
        if 'error' not in self.weather.weatherData:
            self.view.varLocation.set(self.weather.get_location())
            self.view.varCondition.set(self.weather.get_condition_text())
            self.view.varWindSpeed.set(self.weather.get_wind_speed_mph())
            self.view.varWindDir.set(self.weather.get_wind_direction())
            self.view.varIcon.set(self.weather.get_condition_icon())

            script_dir = os.path.dirname(__file__)
            rel_path = self.view.varIcon.get()
            abs_file_path = os.path.join(script_dir, rel_path)
            weather_icon = Image.open(abs_file_path)
            self.update_icon = ImageTk.PhotoImage(weather_icon)
            self.view.label_icon.configure(image=self.update_icon)

            if self.view.varUnits.get() == 1:
                self.view.varTemp.set(self.weather.get_current_temp_f())
                self.view.varFeelsLike.set(self.weather.get_feels_like_f())
            else:
                self.view.varTemp.set(self.weather.get_current_temp_c())
                self.view.varFeelsLike.set(self.weather.get_feels_like_c())

    def handle_button_search(self):
        location = self.view.varSearch.get()
        if location != '':
            self.weather = Weather(location)
            self.update_gui()

    def handle_combo_search(self, location):
        # Parameter location is not used, but fixes search error 1 argument expected but 2 given error
        location = self.view.varSearch.get()
        if len(location) > 3:
            self.mapbox.update_query(location)
            self.view.comboSearch.configure(values=self.mapbox.get_names())
        else:
            self.view.comboSearch.configure(values=[])
