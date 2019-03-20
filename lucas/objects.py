class station:
    def __init__(station, name, temperature, dew_point):
        station.name = name
        station.temperature = temperature
        station.dew_point = dew_point

station1 = station("Omaha", 75, 50)

print(station1.name)
print(station1.temperature)
print(station1.dew_point)
