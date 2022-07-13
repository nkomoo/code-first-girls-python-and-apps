# WORKING WITH CSV FILES
import csv

field_names = ["name", "age"] #square brackets mean list

team_members = [
    {"name": "Jill", "age": 32},
    {"name": "Sarah", "age": 27},
] #curly brackets means its a dictionary

with open("team.csv", "w+") as csv_file:
    spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

    spreadsheet.writeheader()
    spreadsheet.writerows(team_members)

with open("team.csv", "r") as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    for row in spreadsheet:
        print(dict(row))