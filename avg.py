import os, pandas as pd

files = os.listdir('.\\csvs')
for file in files:
    data = pd.read_csv(f'csvs\\{file}')
    avgs = []
    if '<Average>' in data.keys():
        continue
    for i in range(len(data)):  
        avgs.append((float(data['<Open>'][i]) + float(data['<High>'][i]) + float(data['<Low>'][i]) + float(data['<Close>'][i])) / 4.0)
    data['<Average>'] = avgs
    #In file mới có cột avgs từ pd.data và chuyển sang file csv
    data.to_csv(f'csvs\\{file.split(".")[0]}.csv', index = None)
    print(f'done {file.split(".")[0]}.csv')

