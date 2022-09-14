import requests


API_KEY = 'b8958f8bf2f842faaa0160017222806'


class Weather:

    def __init__(self, location: str = 'Heidelberg'):
        self.weatherData = {}
        self.fetch(location)

    def get_location_data(self, name):
        data = self.weatherData['location'][name]
        return str(data)

    def get_city(self):
        return self.get_location_data('name')

    def get_state(self):
        return self.get_location_data('region')

    def get_country(self):
        return self.get_location_data('country')

    def get_time_zone(self):
        return self.get_location_data('tz_id')

    def get_location(self):
        if 'America' in self.get_time_zone():
            return f'{self.get_city()}, {self.get_state()}'
        else:
            return f'{self.get_city()}, {self.get_country()}'

    def get_current_data(self, name):
        data = self.weatherData['current'][name]
        return data if name == 'condition' else str(data)

    def get_current_temp_f(self):
        return self.get_current_data('temp_f') + '\u00B0F'

    def get_current_temp_c(self):
        return self.get_current_data('temp_c') + '\u00B0C'

    def get_condition_text(self):
        condition = self.get_current_data('condition')
        return str(condition['text'])

    def get_condition_icon(self):
        icon = self.get_current_data('weather')
        return icon['icon']

    def get_wind_speed_mph(self):
        return self.get_current_data('wind_mph') + ' mph'

    def get_wind_direction(self):
        return self.get_current_data('wind_dir')

    def get_feels_like_f(self):
        return self.get_current_data('feelslike_f') + '\u00B0F'

    def get_feels_like_c(self):
        return self.get_current_data('feelslike_c') + '\u00B0C'

    def fetch(self, query):
        try:
            url = f'http://api.weatherapi.com/v1/current.json' + \
                  f'?key={API_KEY}&q={query}&aqi=no'
            self.weatherData = requests.get(url).json()
        except:
            self.weatherData = {'error': []}
