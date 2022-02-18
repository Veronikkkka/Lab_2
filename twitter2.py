"""Backend part of web application"""
import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl
import folium
from geopy.geocoders import Nominatim

def request_(nick):
    """
    This function sends a request  to
    twitter api, proccess the json file and
    based in it create map
    If location of user can't be found program just
    skip end
    """
    TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'    
    # Ignore SSL certificate errors
    ctx = ssl.create_default_context()
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE

    # print('')
    acct = nick
    url = twurl.augment(TWITTER_URL,
                        {'screen_name': acct, 'count': '200'})
    print('Retrieving', url)
    connection = urllib.request.urlopen(url, context=ctx)
    data = connection.read().decode()
    js = json.loads(data)
    with open("result.json", "w", encoding="utf-8") as file:
        json.dump(js, file, indent=4)
    
    data = js["users"]
    screen_name_loc = []
    for elem in data:    
        screen_name_loc.append((elem["screen_name"], elem["location"]))
        
    print(screen_name_loc)
    map = folium.Map(location=[46.193239, -82.347307],zoom_start=2)
    fg = folium.FeatureGroup(name="Locations")
    geolocator = Nominatim(user_agent="my_user_agent")
    for elem in screen_name_loc:
        try:
            loc = geolocator.geocode(elem[1])
            fg.add_child(folium.Marker(location=[loc.latitude, loc.longitude],
                                popup=f"{elem[0]}", icon=folium.Icon(color="purple")))
        except:
            pass
        
    map.add_child(fg, name="fg")
    map.add_child(folium.LayerControl())
    map.save('templates/Map.html')
    # print("HERE")
    return True

