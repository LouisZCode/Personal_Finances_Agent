import csv
from config import BALANCE_SHEET_PATH


from functions import read_csvs_in_folder

# TODO -  Read all the CSVs from certain year

year = 2025
read_csvs_in_folder(year)
