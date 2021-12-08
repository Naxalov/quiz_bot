import csv

def read_data_csv(file_name):
    with open(file_name, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        data_github = [row for row in reader]
    return data_github