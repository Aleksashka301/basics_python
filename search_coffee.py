import json
import requests
import os
import folium
from flask import Flask
from dotenv import load_dotenv, find_dotenv
from geopy import distance


def fetch_coordinates(apikey, address):
    base_url = "https://geocode-maps.yandex.ru/1.x"
    response = requests.get(base_url, params={
        "geocode": address,
        "apikey": apikey,
        "format": "json",
    })
    response.raise_for_status()
    found_places = response.json()['response']['GeoObjectCollection']['featureMember']

    if not found_places:
        return None

    most_relevant = found_places[0]
    lon, lat = most_relevant['GeoObject']['Point']['pos'].split(" ")
    return lat, lon


def get_distance_cafes(cafes):
    return cafes['distance']


def creating_map_markers():
    start_point = fetch_coordinates(yandex_api, user_location)
    cafes = []

    for cafe in coffee_shops:
        coffee_shop_details = {}
        end_point = (cafe['Latitude_WGS84'], cafe['Longitude_WGS84'])

        coffee_shop_details['title'] = cafe['Name']
        coffee_shop_details['distance'] = distance.distance(start_point, end_point).km
        coffee_shop_details['latitude'] = cafe['Latitude_WGS84']
        coffee_shop_details['longitude'] = cafe['Longitude_WGS84']

        cafes.append(coffee_shop_details)

    cafes = sorted(cafes, key=get_distance_cafes)
    map = folium.Map(start_point, zoom_start=10)
    folium.Marker(location=start_point, icon=folium.Icon('green'),).add_to(map)

    for cafe in range(5):
        location_cafe = [cafes[cafe]['latitude'], cafes[cafe]['longitude']]
        folium.Marker(location=location_cafe, icon=folium.Icon("red")).add_to(map)
    else:
        map.save('index.html')

    with open('index.html') as web_file:
        return web_file.read()


if __name__ == '__main__':
    load_dotenv(find_dotenv())
    yandex_api = os.getenv('YANDEX_API')
    user_location = input('Укажите, где вы находитесь: ')

    with open('coffee.json', 'r') as file_locations:
        coffee_shops = file_locations.read()

    coffee_shops = json.loads(coffee_shops)

    app = Flask(__name__)
    app.add_url_rule('/', 'start', creating_map_markers)
    app.run('0.0.0.0')
