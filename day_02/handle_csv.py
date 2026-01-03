import csv 

# read as a list
with open(r'C:\Users\admin\Documents\Python\python-to-ml-fast\day_02\data\customers-100.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        pass

# read as a dict
with open(r'C:\Users\admin\Documents\Python\python-to-ml-fast\day_02\data\customers-100.csv', 'r', newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row['Index'], row['First Name'])

data = ['Hassan Khan', 20]
data2 = ['Haniya Khan', 6]
# write to new file
with open(r'C:\Users\admin\Documents\Python\python-to-ml-fast\day_02\data\output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Age'])
    writer.writerow(data)

with open(r'C:\Users\admin\Documents\Python\python-to-ml-fast\day_02\data\output.csv', 'a', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(data2)