import os, pandas as pd

files = os.listdir('.\\txts')
for file in files:
    data = pd.read_csv(f'txts\\{file}')
    data.to_csv(f'csvs\\{file.split(".")[0]}.csv', index = None)
    print(f'done {file.split(".")[0]}.csv')

