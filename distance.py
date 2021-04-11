#python -m pip install haversine
from haversine import haversine, Unit
import urllib.request
import json
from pprint import pprint
import urllib.parse

#example locations
'Boston,MA'
'Paris'

def lat_long(location1, location2): 
    """
    Function that gets the information of a location based on its name. 
    """
    global data_latlong
    print(f"Your departure location is {location1} and destination is {location2}")
    #Imports data from the mapquestapi
    MAPQUEST_API_KEY = 'XxtdAMBvWmSKhAKu0wu0kMXQT8gbOp6b'
    # url = f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location=Babson%20College'
    url1 = (f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={location1}')
    f1 = urllib.request.urlopen(url1)
    response_text1 = f1.read().decode('utf-8')
    data_latlong1 = json.loads(response_text1)
    MBTA_API_KEY = '78c78742ffb14c3cb6b22071c0986b51'

     #Gets the latitude and longitude
    lat1 = data_latlong1["results"][0]["locations"][0]['displayLatLng']['lat']
    long1 = data_latlong1["results"][0]["locations"][0]['displayLatLng']['lng']
    # print(location1)
    # print('lat',lat1)
    # print('long',long1)

    coor1 = (lat1, long1)
    # print(coor1)

    url2 = (f'http://www.mapquestapi.com/geocoding/v1/address?key={MAPQUEST_API_KEY}&location={location2}')
    f2 = urllib.request.urlopen(url2)
    response_text2 = f2.read().decode('utf-8')
    data_latlong2 = json.loads(response_text2)


     #Gets the latitude and longitude
    lat2 = data_latlong2["results"][0]["locations"][0]['displayLatLng']['lat']
    long2 = data_latlong2["results"][0]["locations"][0]['displayLatLng']['lng']
    # print(location2)
    # print('lat',lat2)
    # print('long',long2)
    
    coor2 = (lat2, long2)
    # print(coor2)

    # pprint(response_data)

    # boston = (42.358894,-71.056742)
    # boston = (lat, long)'Chelsea,MA'
    global distance
    dist = haversine(coor1, coor2)
    distance = round(dist, 2)
    # distance = dist
    print(f"The distance between {name1} and {name2} is {distance}km")
    # print(haversine(boston, paris))

# lat_long(name)

def stop(datas):
    """
    Function that prints the closest MBTA stop based on the latitude and longitude. 
    """
    MBTA_API_KEY = '78c78742ffb14c3cb6b22071c0986b51'
    
    #Gets the latitude and longitude
    lat = datas["results"][0]["locations"][0]['displayLatLng']['lat']
    long = datas["results"][0]["locations"][0]['displayLatLng']['lng']
    print('lat',lat)
    print('long',long)

    #imports data from the mbta api
    url1 = (f"https://api-v3.mbta.com/stops?sort=distance&filter%5Blatitude%5D={lat}&filter%5Blongitude%5D={long}")
    f = urllib.request.urlopen(url1)
    response_text1 = f.read().decode('utf-8')
    response_data1 = json.loads(response_text1)
    # pprint(response_data1)

    #Gets the name, at street and on street of the stop
    stop_name = response_data1["data"][0]["attributes"]['name']
    stop_atstreet = response_data1["data"][0]["attributes"]['at_street']
    stop_onstreet = response_data1["data"][0]["attributes"]['on_street'] 
    print(f'The name of the stop is {stop_name}. It is at the street {stop_atstreet} and on the street {stop_onstreet}.')

    #Gets whether the stop is wheelchair accesible
    wheel = response_data1["data"][0]["attributes"]['wheelchair_boarding']
    # print("Has wheelchair access:", response_data1["data"][0]["attributes"]['wheelchair_boarding'])
    
    #Based on the whether the stop is accesible, the result is printed in a more user friendly format
    if wheel == 0: 
        print('There is no information for whether the stop is wheelchair accessible')
    elif wheel == 1:
        print('The stop is accessible to wheelchairs')
    elif wheel == 2:
        print('The stop is inaccessible to wheelchairs')

    # print('lat1', lat)
    # print('long1', long)   

def travel(typer):
    global em
    # if typer == 'train' or typer == 'Train':
    #     em = 41* distance
    if typer == 'train' or typer == 'Train':
        print('Was it an electric of fossil fuel traine?')
        train_type = input()
        if train_type == 'electric' or train_type == 'Electric':
            em = 6 * distance
        else:
            em = 50 * distance
    elif typer == 'bus' or typer == 'Bus':
        em = 104* distance
    elif typer == 'plane' or typer == 'Plane':
        em = 133 * distance
    elif typer == 'car' or typer == 'Car':
        em = 171 * distance

    em = round(em, 2)
    em_round = round(em * 2, 2)
    print(f'You produced {em}g of CO2 on your trip and {em_round}g of CO2 for a round trip')


# stop(data_latlong)
# print('lat2', lat)
# print('long2', long)

def distance_calc():
    """
    Function that adds the input at the beggining and puts the two previous functions together
    """
    global name1
    global name2
    global name3
    print('Input your departure location')
    name1 = input()
    # name1 = 'Boston,MA'

    print('Input your departure location')
    name2 = input()
    # name2 = 'Paris'
    lat_long(name1, name2)
    # stop(data_latlong)

    print("Were you travelling by car, bus, train or plane")
    name3 = input()
    travel(name3)


def main():
    distance_calc()


if __name__ == "__main__":
    main()

#example locations
'Boston,MA'
'Wellesley,MA'
'Chelsea,MA'
'Brookline,MA'
