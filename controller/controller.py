from view.view import View
from model.weather import Weather
from model.mapbox import MapBox


class Controller:

    def __init__(self) -> None:
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

    def handle_combo_search(self):
        location = self.view.varSearch.get()
        if len(location) > 3:
            self.mapbox.update_query(location)
            self.view.comboSearch.configure(values=self.mapbox.get_names())
        else:
            self.view.comboSearch.configure(values=[])
