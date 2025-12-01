"""
Here you find all the functions related toprocess and prepare the
data for ingestion or read for an LLM or Human
"""

from config import BALANCE_SHEET_PATH
import glob
import pandas as pd

def read_csvs_in_folder(year : int) -> str:

    all_files = glob.glob(f"{BALANCE_SHEET_PATH}/{year}/*.csv")

    all_dataframes = []
    for file in all_files:
        df = pd.read_csv(file)
        df = df.to_markdown
        all_dataframes.append(df)
        
    return all_dataframes

