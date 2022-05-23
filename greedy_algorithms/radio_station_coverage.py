stations = {
    "kone" : ['id', 'nv', 'ut', 'az'],
    "ktwo" : ['wa', 'id', 'mt'],
    "kthree" : ['or', 'nv', 'ca'],
    "kfour" : ['nv', 'ut'],
    "kfive" : ['ca', 'az']
}

def get_stations(stations):
    states_to_cover = set()
    for k, v in stations.items():
        states_to_cover |= set(v)

    stations_to_use = []
    
    while states_to_cover:
        # get the best station
        best_station = None
        best_station_covers = set()
        for station in stations:
            station_covers = states_to_cover & set(stations[station])
            if len(station_covers) > len(best_station_covers):
                best_station = station
                best_station_covers = station_covers

        # add the best station to stations_to_use and update the states_to_cover
        # and unprocessed_stations
        stations_to_use.append(best_station)
        states_to_cover -= set(best_station_covers)


    return stations_to_use


print(get_stations(stations))