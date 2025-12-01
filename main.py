import csv
from config import BALANCE_SHEET_PATH
import pandas as pd
import glob

# TODO -  Read all the CSVs from certain year

year = 2025

all_files = glob.glob(f"{BALANCE_SHEET_PATH}/{year}/*.csv")


all_dataframes = []
for file in all_files:
    df = pd.read_csv(file)
    all_dataframes.append(df)

print(all_dataframes)
