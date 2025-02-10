'''
This is the main program. 
You should read the packaging.txt in the data folder.
Each line contains one package description. 
You should parse the package description using parse_packaging()
print the total number of items in the package using calc_total_units()
along with the unit using get_unit()
place each package in a list and save in JSON format.

Example:

    INPUT (example data/packaging.txt file):
    
    12 eggs in 1 carton
    6 bars in 1 pack / 12 packs in 1 carton

    OUTPUT: (print to console)

    12 eggs in 1 carton => total units: 12 eggs
    6 bars in 1 pack / 12 packs in 1 carton => total units: 72 bars

    OUTPUT (example data/packaging.json file):
    [
        [{ 'eggs' : 12}, {'carton' : 1}],
        [{ 'bars' : 6}, {'packs' : 12}, {'carton' : 1}],
    ]    
'''

# TODO: Write code
import json

def parse_packaging(line):
    return [{w[1]: int(w[0])} for w in (p.split() for p in line.split(' in ')) if len(w) == 2]

def calc_total_units(parsed_data):
    total = 1
    unit = list(parsed_data[0].keys())[0] if parsed_data else ""
    for item in parsed_data:
        total *= list(item.values())[0]
    return total, unit

def main():
    try:
        with open('data/packaging.txt') as file:
            packages = []
            for line in file:
                parsed = parse_packaging(line.strip())
                total, unit = calc_total_units(parsed)
                print(f"{line.strip()} => total units: {total} {unit}")
                packages.append(parsed)
        with open('data/packaging.json', 'w') as json_file:
            json.dump(packages, json_file, indent=4)
    except FileNotFoundError:
        print("File not found.")

if __name__ == "__main__":
    main()