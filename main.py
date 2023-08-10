import folium

m = folium.Map(location=[40.7128, -74.0060], zoom_start=13)
#folium.Marker(location=[40.7128, -74.0060], popup='New York City').add_to(m)
#folium.Marker(location=[40.71971485419323, -73.98778579840273], popup='New York Sound').add_to(m)

#trying to add sound


folium.Marker(
    location=[40.70728436132522, -74.01821652294706],
    popup=folium.Popup('<b>Soutch Cove Park, NYC</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/sound01.mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/soutchcovepark.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)

folium.Marker(
    location=[40.71150021146467, -74.0126045785288],
    popup=folium.Popup('<b>World Trade Center, NYC</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/worldtradecenter.mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/worldtradecenter.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)

folium.Marker(
    location=[40.71448360094586, -74.00521952993573],
    popup=folium.Popup('<b>Hall des Lumières, NYC</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Hall des Lumières.mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Hall des Lumières.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)

folium.Marker(
    location=[40.7257391288523, -74.00447358986794],
    popup=folium.Popup('<b>6th Ave, NYC</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/6th Ave.mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/6th Ave.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)

folium.Marker(
    location=[40.725207010418394, -74.00462488721533],
    popup=folium.Popup('<b>6th Ave, NYC</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/6th Ave2.mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/6th Ave2.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)


folium.Marker(
    location=[40.7310324823632, -73.99729930156094],
    popup=folium.Popup('<b>Washington Square Park, NYC</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Washington Square Park .mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Washington Square Park.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)

folium.Marker(
    location=[40.73439702463118, -74.00218427244802],
    popup=folium.Popup('<b>55 bar Greenwich village, NYC</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/55 bar Greenwich village.mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/55 bar Greenwich village.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)

folium.Marker(
    location=[40.73983257536489, -74.00827295932538],
    popup=folium.Popup('<b>High Line, NYC</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/High Line.mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/High Line.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)


folium.Marker(
    location=[40.69275986195592, -74.01677528853554],
    popup=folium.Popup('<b>Governors Island</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Governors Island.mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Governors Island.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)

folium.Marker(
    location=[40.74971251529183, -73.98619376257429],
    popup=folium.Popup('<b>Empire State Building</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Empire State Building.mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Empire State Building.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)

folium.Marker(
    location=[40.75065293669419, -73.99343486712027],
    popup=folium.Popup('<b>Train Station, near Madison Square Garden</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Madison Square Garden .mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Madison Square Garden.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)

folium.Marker(
    location=[40.75232365454732, -73.9932078197861],
    popup=folium.Popup('<b>8th Ave, NYC</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Madison2.mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Madison2.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)

folium.Marker(
    location=[40.753908777687194, -73.98134643326594],
    popup=folium.Popup('<b>500 Fifth Avenue, NYC</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/500 Fifth Avenue.mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/500 Fifth Avenue.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)

folium.Marker(
    location=[40.6430372294819, -74.073553452928],
    popup=folium.Popup('<b>500 Ferry Terminal Viaduct</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Ferry Terminal Viaduct.mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Ferry Terminal Viaduct.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)

folium.Marker(
    location=[41.59393908438857, -73.49781373111168],
    popup=folium.Popup('<b>500 Sherman Church Parsonage</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Sherman Church Parsonage.mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Sherman Church Parsonage.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)

folium.Marker(
    location=[40.68767134112016, -73.97194201504175],
    popup=folium.Popup('<b>500 Lafayette Ave</b><br><audio controls><source src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Lafayette Ave.mp3" type="audio/mpeg"></audio> <img src="/Users/sivan/PycharmProjects/SonificatingCities/tools/Lafayette Ave.png"style="width: 200px;">', max_width=240),
    icon=folium.Icon(color='blue')
).add_to(m)



m.save('/Users/sivan/map.html')
