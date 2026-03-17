import csv
from collections import Counter

def analyze_csv(filename, column_index):
    with open(filename, 'r') as file:
        reader = list(csv.reader(file))

    rows = len(reader) - 1
    column_values = [row[column_index] for row in reader[1:]]

    unique_values = set(column_values)
    counts = Counter(column_values)

    print("Total Rows:", rows)
    print("Unique Values:", unique_values)
    print("Counts:", counts)


analyze_csv("data.csv", 1)