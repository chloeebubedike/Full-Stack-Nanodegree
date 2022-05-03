import csv

total_sunshine_hours = []

with open('healthy_lifestyle_city_2021.csv', 'r') as city_file:
    spreadsheet = csv.DictReader(city_file)
    for row in spreadsheet:

        total_sunshine_hours.append((row['Sunshine hours(City)']))

    print(int(total_sunshine_hours))

