import regex as re
import os
import pandas as pd 

def clean_data(csv_path, year):
    '''keeps just the table entries from the correct year -- 
    because spotify charts goes by weeks and some years start mid week'''
    df = pd.read_csv(csv_path)
    df = df[df['week start date'].str[:4] == year]
    output_name = f'weekly_top200/{year}_weekly_all_locations_top200.csv'
    df.to_csv(output_name, index = False)
    print(f'{year}_weekly_all_locations_top200.csv saved to file')



def file_select(dir_list):
    '''returns a list of files from a given directory that are weekly top charts'''
    files = os.listdir(dir_list)
    word = 'weekly'
    list_files = []
    for i in files:
        if re.search(rf'\b\w*{word}\w*\b', str(i), flags=re.I):
            list_files.append(i)
    return list_files

## Cleaning scrape_data and output to weekly_top200 folder
for idx, file in enumerate(file_select('scrape_data')):
    year = file_select('scrape_data')[idx][:4]
    path = os.path.join('scrape_data', file)
    clean_data(path, year)