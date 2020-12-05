"""

"""

from itertools import permutations, combinations_with_replacement

city_temps = {
    "Casa_Grande": [76, 69, 60, 64, 69],
    "Chandler": [77, 68, 61, 65, 67],
    "Flagstaff": [46, 35, 33, 40, 44],
    "Lake Havasu City": [71, 65, 63, 66, 68],
    "Sedona": [62, 47, 45, 51, 56]
}

hotel_rates = {
    "Motel 6": 89,
    "Best Western": 109,
    "Holiday Inn Express": 115,
    "Courtyard by Marriott": 229,
    "Residence Inn": 199,
    "Hampton Inn": 209
}

HOTEL_BUDGET = 850
DAYS = 5

combs = list(combinations_with_replacement(hotel_rates.keys(), DAYS))
perms = list(permutations(city_temps.keys(), DAYS))


def avg_temp(route):
    temp_route = [city_temps[route[i]][i] for i in range(len(route))]
    return sum(temp_route) / len(route)


temp_route = max(perms, key=lambda t: avg_temp(t))


def cost_route(t):
    return sum([hotel_rates[x] for x in t])


cost_hotel = min(combs, key=lambda t: HOTEL_BUDGET - cost_route(t) if HOTEL_BUDGET >= cost_route(t) else HOTEL_BUDGET)

if __name__ == "__main__":
    cities = list(city_temps.keys())
    hotels = list(hotel_rates.keys())
    # ..
    print(f'Here is your best route: {temp_route} the average of the daily max temp. is {avg_temp(temp_route)}F')
    # ..
    print(f'To max out your hotel budget, stay at these hotels: {cost_hotel}, totaling ${cost_route(cost_hotel)}')
