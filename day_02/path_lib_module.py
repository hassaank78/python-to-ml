from pathlib import Path
input_dir = Path('data')
for files in input_dir.iterdir():
    if files.is_dir():
        print(files)