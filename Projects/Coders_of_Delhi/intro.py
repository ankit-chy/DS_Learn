import json


# Function to load data from a JSON file
def load_data_from_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

data = load_data_from_json_file('DS_Learn/Projects/Coders_of_Delhi/data.json')

print(data)
print("Data loaded successfully from data.json")