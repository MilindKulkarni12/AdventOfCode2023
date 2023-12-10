import time

with open('./input.txt', 'r') as r:
    data = r.readlines()

seeds = list(map(int, data[0].split(':', 1)[1].split()))
# print(seeds)

i = 3
seed_to_soil_map = []
while len(data[i].strip('\n')) > 0:
    seed_to_soil_map.append(list(map(int, data[i].split())))
    i += 1

i += 2
soil_to_fertilizer_map = []
while len(data[i].strip('\n')) > 0:
    soil_to_fertilizer_map.append(list(map(int, data[i].split())))
    i += 1

i += 2
fertilizer_to_water_map = []
while len(data[i].strip('\n')) > 0:
    fertilizer_to_water_map.append(list(map(int, data[i].split())))
    i += 1

i += 2
water_to_light_map = []
while len(data[i].strip('\n')) > 0:
    water_to_light_map.append(list(map(int, data[i].split())))
    i += 1

i += 2
light_to_temperature_map = []
while len(data[i].strip('\n')) > 0:
    light_to_temperature_map.append(list(map(int, data[i].split())))
    i += 1

i += 2
temperature_to_humidity_map = []
while len(data[i].strip('\n')) > 0:
    temperature_to_humidity_map.append(list(map(int, data[i].split())))
    i += 1

i += 2
humidity_to_location_map = []
while i < len(data):
    humidity_to_location_map.append(list(map(int, data[i].split())))
    i += 1

# print(seed_to_soil_map)
# print(soil_to_fertilizer_map)
# print(fertilizer_to_water_map)
# print(water_to_light_map)
# print(light_to_temperature_map)
# print(temperature_to_humidity_map)
# print(humidity_to_location_map)


def get_record(src_to_dest_map, val):
    for std in src_to_dest_map:
        dest, src, lim = std
        if src <= val <= (src + lim):
            return dest + val - src
    return val

def get_record2(src_to_dest_map, val):
    for std in src_to_dest_map:
        src, dest, lim = std
        if src <= val <= (src + lim):
            return dest + val - src
    return val


def part1(seeds):
    locations = []
    for seed in seeds:
        soil = get_record(seed_to_soil_map, seed)
        fertilizer = get_record(soil_to_fertilizer_map, soil)
        water = get_record(fertilizer_to_water_map, fertilizer)
        light = get_record(water_to_light_map, water)
        temperature = get_record(light_to_temperature_map, light)
        humidity = get_record(temperature_to_humidity_map, temperature)
        location = get_record(humidity_to_location_map, humidity)
        locations.append(location)
        # print(soil)
        # print(fertilizer)
        # print(water)
        # print(light)
        # print(temperature)
        # print(humidity)
        # print(location)

    return min(locations)


def in_range(seed, seeds):
    for i in range(0, len(seeds), 2):
        if seeds[i] <= seed < seeds[i] + seeds[i+1]:
            return True
    return False


def part2(seeds):
    location = 0
    while location < 41222969:
        humidity = get_record2(humidity_to_location_map, location)
        temperature = get_record2(temperature_to_humidity_map, humidity)
        light = get_record2(light_to_temperature_map, temperature)
        water = get_record2(water_to_light_map, light)
        fertilizer = get_record2(fertilizer_to_water_map, water)
        soil = get_record2(soil_to_fertilizer_map, fertilizer)
        seed = get_record2(seed_to_soil_map, soil)

        if in_range(seed, seeds):
            return location, seed

        location += 1
    return -1


location = part1(seeds)
# print(location)
start_time = time.time()
print(part2(seeds))
end_time = time.time()
print(round(end_time - start_time, 2))
# 457,535,844
# 41,222,969
