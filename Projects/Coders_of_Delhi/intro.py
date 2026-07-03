import json


# Function to load data from a JSON file
def load_data_from_json_file(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    return data

data = load_data_from_json_file('DS_Learn/Projects/Coders_of_Delhi/data.json')

#print(data)
#print("Data loaded successfully from data.json")
#print(type(data))


#function to display the data in a readable format
def display_data(data):
    print("Users, their friends and liked pages:\n")
    for users in data['users']:
        print(f"ID:{users['id']} {users['name']} is friends with : {users['friends']} and liked pages are : {users['liked_pages']}")

    print("\nPages Information:\n")
    for page in data['pages']:
        print(f"{page['id']}: {page['name']}")

print("Displaying data in a readable format:\n")
display_data(data)