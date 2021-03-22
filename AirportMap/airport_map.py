from plotly import offline
import csv


filename = 'airports.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)


    ident, name, lat, lon, home_link, texts = [], [], [], [], [], []

    for row in reader:
        if row[2] == 'large_airport':
            ident.append(row[1])

            lat.append(row[4])
            lon.append(row[5])

            text = f"Name:{row[3]}<br />City:{row[10]}"
            texts.append(text)

    data = [{
        'type': 'scattergeo',
        'lon': lon,
        'lat': lat,
        'text': texts,
        'marker': {
            'color': 'rgb(40, 60, 80)',
            'size': 5
            }
    }]

    layout = {
        'title' : "Map of Airports"
    }
    fig = {'data': data, 'layout': layout}

    offline.plot(fig, filename="mapofairport.html")




