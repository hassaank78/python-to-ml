with open('../data/abc.html', 'r') as f:
    content = f.readlines()
    print(content)

with open('../data/output.txt', 'a') as f:
    f.write('Hello, World!\n')