import csv

dictionary = [{'task': 'Grocery store', 'status': 'Done'}, {'task':'Walk the dog', 'status': 'Not Done'}, {'task': 'Cook Dinner', 'status': 'Not Done'}]

try: 
    with open("test.csv", "r", newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            print(row["task"], row["status"])

except FileNotFoundError:
    with open("test.csv", "w", newline="") as f:
        fieldnames = ['task', 'status']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(dictionary)