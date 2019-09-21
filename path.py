from node import Node

searcher_distance = Node('searcher_distance', [])
searcher_number = Node('searcher_number', [searcher_distance])
location_check = Node('location_check', [searcher_number])
searcher_location = Node('searcher_location', [location_check])
choose_type = Node('choose_type', [searcher_location])
index = Node('index',[choose_type])

ROOT = index
