import csv 
import sys
sys.path.append('..')
from day_01.main import mean

with open('data/sample_dataset.csv', 'r') as f:
    reader = csv.reader(f)
    column_names = next(reader)
    num_cols = len(column_names)
    data = list(reader)
    num_rows = len(data)
    f.close()
print(f'Number of rows {num_rows}')
print(f'Number of cols {num_cols}')
print(f'Column names {column_names}')

missing_values = [0] * num_cols
for row in data:
    for i, val in enumerate(row):
        if not val.strip():
            missing_values[i] += 1

print('Number of missing values in each column')
for name, count in zip(column_names, missing_values):
    print(f'{name}: {count}')

# 1. Identify numeric column
is_numeric = [0] * num_cols
for row in data:
    for i, value in enumerate(row):
        try:
            float(value)
            is_numeric[i] = True
        except:
            print(i)
            is_numeric[i] = False

print(is_numeric)

# 2. find min, max and mean of each column

for i in range(num_cols):
    if is_numeric[i]:
        column_name = column_names[i]
        values = []
        for row in data:
            values.append(float(row[i]))
        
        print(f'min, max, and mean for {column_name}')
        print(f'1. min: {min(values)}')
        print(f'2. max: {max(values)}')
        print(f'3. mean {mean(values)}')

            

            
