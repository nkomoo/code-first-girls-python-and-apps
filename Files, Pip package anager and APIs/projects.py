# Program that read data about trees from a file
# to find the shortest tree.
import csv

with open("trees.csv", "r") as csv_file:
    spreadsheet = csv.DictReader(csv_file)

    heights = []

for row in spreadsheet:
    tree_height = row["height"]
    heights.append(tree_height)

shortest_height = min(heights)
print(shortest_height)

# Application Programming Interface - a way for different programs to interact.
