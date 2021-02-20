import scraper_functions as scrape
import pandas as pd
import os
from tqdm import tqdm
from multiprocessing import Pool

## Scraper Inputs ##
start_date = '2020-12-25'
end_date = '2021-02-20'

## File Paths ##
root_path = "scrape_data"
dir_2020 = os.path.join(root_path, "2020")
dir_2021 = os.path.join(root_path, "2021")

# check to see if the scrape_data dir exists -- if not, create one 
if not os.path.exists(root_path):
    os.makedirs(root_path)

# check to see if the sub directories for the years exsits -- if not, create them 
if not os.path.exists(dir_2020):
    os.makedirs(dir_2020)
if not os.path.exists(dir_2021):
    os.makedirs(dir_2021)

loc_code, loc_name = scrape.get_locations()
dates = scrape.list_dates(start_date, end_date)

df = pd.DataFrame()
for date in tqdm(dates):
    for i in tqdm(range(len(loc_code))):
        loc_link = scrape.get_chart_url(loc_code[i], "weekly", date[0],date[1])
        chart_df = scrape.scrape_spotify(loc_link, loc_name[i], date[0])
        df = pd.concat([df, chart_df])
    if date[:4] == '2020':
        dir_path = dir_2020
    else:
        dir_path = dir_2021
    scrape.output(df, dir_path, date)



