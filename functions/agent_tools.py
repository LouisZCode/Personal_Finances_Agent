from langchain.tools import tool
from config import BALANCE_SHEET_PATH
import glob
import pandas as pd
import tabulate

@tool(
    "read_balance_sheet",
    parse_docstring=True,
    description="reads the balances and movements inside the balance sheet"
)
def read_balance_sheet(year : int) -> str:
    """
    Description:
        Lets you access the balance sheet of the specified year, if no year is specified, reads all the balance sheets.

    Args:
        year (int): the year the user is interested in knowing more about

    Returns:
        gives back the balance sheet information of that years movements

    Raises:
        Lets you know if there is no information about that year
    """
    all_files = glob.glob(f"{BALANCE_SHEET_PATH}/{year}/*.csv")

    all_dataframes = []
    for file in all_files:
        df = pd.read_csv(file)
        df = df.to_markdown()
        all_dataframes.append(df)
        
    return all_dataframes