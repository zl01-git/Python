import folium
from zones import Marker, markers, circuts
from geopy import distance
import time



omsk = Marker("omsk", "omsk", 54.991416, 73.364253)

m = folium.Map(location=[omsk.lat, omsk.long], zoom_start=11)


for circut in circuts:
    folium.Circle(location=[circut.lat, circut.long],
                  radius=circut.radius, 
                  tooltip=circut.name, 
                  popup=circut.name
                  ).add_to(m)
    for marker in markers:
        dist = distance.geodesic([circut.lat, circut.long], 
                                 [marker.lat, marker.long]
                                 ).km * 1000
        if dist < circut.radius:
            folium.Marker(location=[marker.lat, marker.long], 
                          tooltip=marker.name, 
                          popup=marker.descriptions
                          ).add_to(m)
    
    m = folium.Map(location=[omsk.lat, omsk.long], 
                   zoom_start=11
                   )

# folium.Circle(location=[circuts[1].lat, circuts[1].long], 
#               radius=circuts[1].radius, 
#               tooltip=circuts[1].name, 
#               popup=circuts[1].name
#               ).add_to(m)



