class station:
    def __init__(station, name, temperature, dew_point):
        station.name = name
        station.temperature = temperature
        station.dew_point = dew_point

omaha_station = station("Omaha", 75, 50)
kansas_city_station = station("Kansas City", 80, 55)
oklahoma_city_station = station("Oklahoma city", 90, 60)

print(omaha_station.name)
print(omaha_station.temperature)
print(omaha_station.dew_point)

print(kansas_city_station.name)
print(kansas_city_station.temperature)
print(kansas_city_station.dew_point)

print(oklahoma_city_station.name)
print(oklahoma_city_station.temperature)
print(oklahoma_city_station.dew_point)
