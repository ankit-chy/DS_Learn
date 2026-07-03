import json


# Function to load data from a JSON file
def load_data_from_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


