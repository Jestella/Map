import folium
map = folium.Map(location=[43, -79], zoom_start=6, tiles="Stamen Terrain")

map.add_child(folium.Marker(location=[38.2, -99.1], popup="Hi I am a Marker", icon=folium.Icon(color="orange")))
fg = folium.FeatureGroup(name="My Map")
map.add_child(fg)

map.save("Map1.html")