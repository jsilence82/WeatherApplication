import requests

api_key = "pk.eyJ1IjoianNpbGVuY2U4MiIsImEiOiJjbDR5Y2t6bWsxb21vM2JtemRkNjdvY3g1In0.XxU_j_M6oVJi7TTINiGW2w"


class MapBox:

    def __init__(self, query='Heidelberg', limit=5):
        self.query = query
        self.limit = limit
        self.searchData = {}

        self.fetch()

    def get_names(self) -> list:
        names = []
        for location in self.searchData:
            place_name = location['place_name'].split(', ')
            if 'United States' in place_name:
                names.append(f'{place_name[0]}, {place_name[1]}')
            else:
                names.append(f'{place_name[0]}, {place_name[2]}')

        return names

    def update_query(self, query):
        self.query = query
        self.fetch()

    def fetch(self):
        url = f'https://api.mapbox.com/geocoding/v5/mapbox.places/' + \
              f'{self.query}.json?access_token={api_key}' + \
              f'&limit={self.limit}&types=place'
        try:
            self.searchData = requests.get(url).json()['features']
        except:
            print(f'MapBox exception: {url}')
