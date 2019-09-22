from node import Node

ammenities = Node('ammenities', [])

special_needs = Node('special_needs', ammenities)

special_needs_ask = Node('special_needs_ask', [ammenities,special_needs ])

accommodation_time = Node('accommodation_time', [special_needs_ask])
food_options = Node('food_options', [accommodation_time])

food = Node('food', [food_options, accommodation_time])

results = Node('results', [])

searcher_distance = Node('searcher_distance', [results])

searcher_number = Node('searcher_number', [searcher_distance])
offerer_number = Node('offerer_number', [food])

location_check = Node('location_check', [searcher_number])
offerer_location_check = Node('offerer_location_check', [offerer_number])

searcher_location = Node('searcher_location', [location_check])
offerer_location = Node('offerer_location', [offerer_location_check])

choose_type = Node('choose_type', [searcher_location, offerer_location])
index = Node('index',[choose_type])

ROOT = index
